import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import View # Nhập Lớp View gốc của Django để kế thừa
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# --- LỚP 1: XỬ LÝ ĐĂNG KÝ ---
@method_decorator(csrf_exempt, name='dispatch')
class DangKyView(View): 
    
    # Hàm post() trong OOP tự động xử lý khi Frontend gửi dữ liệu POST
    def post(self, request):
        try:
            data = json.loads(request.body)
            ten_tai_khoan = data.get('username')
            mat_khau = data.get('password')
            email = data.get('email', '')

            if User.objects.filter(username=ten_tai_khoan).exists():
                return JsonResponse({'thanh_cong': False, 'loi': 'Tên tài khoản này đã có người sử dụng!'})

            User.objects.create_user(username=ten_tai_khoan, email=email, password=mat_khau)
            return JsonResponse({'thanh_cong': True, 'thong_bao': 'Tạo tài khoản thành công!'})
            
        except Exception as e:
            return JsonResponse({'thanh_cong': False, 'loi': 'Dữ liệu gửi lên bị lỗi.'})


# --- LỚP 2: XỬ LÝ ĐĂNG NHẬP ---
@method_decorator(csrf_exempt, name='dispatch')
class DangNhapView(View):
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            ten_tai_khoan = data.get('username')
            mat_khau = data.get('password')

            user = authenticate(request, username=ten_tai_khoan, password=mat_khau)

            if user is not None:
                login(request, user)
                return JsonResponse({'thanh_cong': True, 'thong_bao': 'Đăng nhập thành công!', 'user': ten_tai_khoan})
            else:
                return JsonResponse({'thanh_cong': False, 'loi': 'Sai tên tài khoản hoặc mật khẩu!'})
                
        except Exception as e:
            return JsonResponse({'thanh_cong': False, 'loi': 'Dữ liệu gửi lên bị lỗi.'})


# --- LỚP 3: XỬ LÝ QUÊN MẬT KHẨU ---
@method_decorator(csrf_exempt, name='dispatch')
class QuenMatKhauView(View):
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            ten_tai_khoan = data.get('username')
            email = data.get('email')
            mat_khau_moi = data.get('new_password')

            try:
                user = User.objects.get(username=ten_tai_khoan, email=email)
                user.set_password(mat_khau_moi)
                user.save() 
                return JsonResponse({'thanh_cong': True, 'thong_bao': 'Đổi mật khẩu mới thành công!'})
                
            except User.DoesNotExist:
                return JsonResponse({'thanh_cong': False, 'loi': 'Tên tài khoản hoặc email không khớp!'})
                
        except Exception as e:
            return JsonResponse({'thanh_cong': False, 'loi': 'Dữ liệu gửi lên bị lỗi.'})
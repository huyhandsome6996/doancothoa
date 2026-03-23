from django.urls import path
from .views import DangKyView, DangNhapView, QuenMatKhauView

urlpatterns = [
    # Nhớ thêm .as_view() khi gọi Class
    path('dang-ky/', DangKyView.as_view()),
    path('dang-nhap/', DangNhapView.as_view()),
    path('quen-mat-khau/', QuenMatKhauView.as_view()),
]
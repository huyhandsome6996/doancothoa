#!/usr/bin/env bash
# Tự động dừng nếu có lỗi
set -o errexit

# Cài đặt các thư viện
pip install -r requirements.txt

# Cập nhật CSDL (Lưu ý: Nếu file này nằm ngoài thư mục core thì dùng lệnh dưới)
python core/manage.py migrate

# TỰ ĐỘNG TẠO ADMIN (User: admin / Pass: MatKhau123@)
python core/manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'MatKhau123@')
    print(">>> DA TAO ADMIN MAC DINH SUCCESS!")
END
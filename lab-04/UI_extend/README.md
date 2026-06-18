# Lab 04 - UI Extend (Secure Chat Cyberpunk)

Đây là phiên bản nâng cấp của Lab 04 với giao diện Web (UI) sử dụng Flask theo phong cách **Cyberpunk** độc đáo. Bao gồm 2 project:

1. **aes_rsa_socket_UI**: Secure Chat qua Socket sử dụng AES (mã hóa dữ liệu) và RSA (trao đổi khóa AES).
2. **dh_aes_socket_UI**: Secure Chat qua Socket sử dụng AES (mã hóa dữ liệu) và Diffie-Hellman (trao đổi khóa chung).

## Cài đặt thư viện (Requirements)

Cần cài đặt Flask và các thư viện mã hóa:
```bash
pip install flask pycryptodome cryptography
```

## Cách chạy

Với mỗi thư mục (`aes_rsa_socket_UI` hoặc `dh_aes_socket_UI`):

**Bước 1:** Khởi động Server. Mở terminal trong thư mục bài tập tương ứng và chạy:
```bash
python server.py
```

**Bước 2:** Khởi động Client. Mở một (hoặc nhiều) terminal khác ở cùng thư mục và chạy:
```bash
python client.py
```

Trình duyệt sẽ tự động mở lên giao diện Chat phong cách Cyberpunk. Bạn có thể mở nhiều cửa sổ terminal khác nhau để chạy nhiều client cùng lúc và chat với nhau an toàn.

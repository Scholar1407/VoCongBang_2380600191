# Lab 04

Kết hợp các thuật toán Hash, Diffie-Hellman, AES và RSA qua mô hình Socket (Client-Server).

## Cấu trúc thư mục
- `aes_rsa_socket`: Giao tiếp Socket dùng AES để mã hóa tin nhắn và RSA để trao đổi khóa.
- `dh_key_pair`: Demo trao đổi khóa Diffie-Hellman.
- `hash`: Demo các hàm băm.
- `UI_extend`: Bản nâng cấp có giao diện Web UI (Flask) phong cách Cyberpunk (Xem chi tiết trong thư mục `UI_extend`).

## Cài đặt thư viện (Requirements)
```bash
pip install pycryptodome cryptography
```

## Cách chạy
Mỗi bài tập sẽ có file `server.py` và `client.py` riêng biệt.
1. Mở terminal tại thư mục bài tập cần chạy, chạy server trước:
```bash
python server.py
```
2. Mở các terminal khác, chạy client để giao tiếp với server:
```bash
python client.py
```

<div align="center">

**Môn học: Thực hành bảo mật thông tin nâng cao**

**Cre:** Võ Công Bằng (MSSV: 2380600191)

---

### 💻 Technologies & Tools

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-pycryptodome-red?style=for-the-badge&logo=letsencrypt&logoColor=white)
![Socket](https://img.shields.io/badge/Socket-Networking-blue?style=for-the-badge&logo=cisco&logoColor=white)
![HTML/CSS/JS](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white)

</div>

## 📖 Giới thiệu (Introduction)

Dự án bao gồm các labs thực hành liên quan đến lập trình Python cơ bản, kiến trúc Client-Server (Socket), cùng với việc triển khai các thuật toán mã hóa và bảo mật thông tin như mã hóa đối xứng, bất đối xứng, băm và trao đổi khóa.

## 📂 Cây thư mục (Directory Structure)

```text
📦 VoCongBang_2380600191
 ┣ 📂 Lab-01/
 ┃ ┗ 📜 hello.py (Làm quen Python cơ bản)
 ┣ 📂 lab-02/
 ┃ ┗ 📂 ex01/ (Các bài tập thực hành Python cơ bản)
 ┣ 📂 lab-03/
 ┃ ┣ 📜 api.py (API Server mã hóa)
 ┃ ┣ 📜 ceasar_cipher.py (Mã hóa Caesar)
 ┃ ┣ 📜 rsa_cipher.py (Mã hóa RSA)
 ┃ ┗ 📜 ecc_event.py (Mã hóa ECC)
 ┣ 📂 lab-04/
 ┃ ┣ 📂 aes_rsa_socket/ (Giao tiếp Socket bằng AES + RSA)
 ┃ ┣ 📂 dh_key_pair/ (Trao đổi khóa Diffie-Hellman)
 ┃ ┣ 📂 hash/ (Ứng dụng Hàm băm / Hashing)
 ┃ ┗ 📂 UI_extend/ (Nâng cấp giao diện Web UI - Secure Chat)
 ┃   ┣ 📂 aes_rsa_socket_UI/ (Cyberpunk UI cho AES-RSA Socket)
 ┃   ┗ 📂 dh_aes_socket_UI/ (Cyberpunk UI cho Diffie-Hellman-AES Socket)
 ┣ 📜 requirement.txt (Danh sách thư viện phụ thuộc)
 ┗ 📜 README.md (Tài liệu giới thiệu chung)
```

---

## 🛠️ Thư viện sử dụng (Libraries)

Dự án sử dụng một số thư viện quan trọng để hiện thực hóa bảo mật:

- **`pycryptodome`**: Cung cấp các thuật toán mã hóa chuẩn (AES, RSA, Pad/Unpad).
- **`cryptography`**: Cung cấp công cụ sinh tham số và trao đổi khóa (Diffie-Hellman, HKDF).
- **`flask`**: Micro-framework xây dựng giao diện Web cho hệ thống chat.
- **Mạng**: Sử dụng module `socket` và `threading` có sẵn trong môi trường Python.

---

## 🚀 Hướng dẫn cài đặt (Installation)

1. Đảm bảo môi trường đã cài đặt Python.
2. Mở terminal tại thư mục gốc của dự án, cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirement.txt
   ```
   Hoặc cài đặt thủ công:
   ```bash
   pip install flask pycryptodome cryptography
   ```

_Để xem hướng dẫn chạy chi tiết cho từng bài cụ thể, vui lòng tham khảo file `README.md` bên trong mỗi thư mục Lab._

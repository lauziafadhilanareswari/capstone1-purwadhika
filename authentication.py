### Sitem autentikasi untuk admin/HR

# database user admin
admin_users = {
    "admin123": {
        "password": "Admin123!",
        "nama": "Administrator",
        "role": "admin"
    },
    "hr001": {
        "password": "Hr123@",
        "nama": "HR Manager",
        "role": "HR"
    }
}

## validasi login admin
def validasi_login(username, password):
    if username in admin_users:
        if admin_users[username]["password"] == password:
            return True, admin_users[username]
    return False, None

## login admin
def login_admin():
    print("\n" + "="*60)
    print("Login Admin - Sistem Manajemen PT Sukses Sejahtera Aamiin".center(60))
    print("="*60)

    percobaan = 0
    max_percobaan = 3

    while percobaan < max_percobaan:
        print(f"\nPercobaan ke-{percobaan+1} dari {max_percobaan}".center(60))
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        sukses, user_data = validasi_login(username, password)

        if sukses:
            print("\nLogin Berhasil.".center(60))
            return True, user_data
        else:
            percobaan += 1
            if percobaan < max_percobaan:
                print("\nUsername atau password salah. Silakan coba lagi.".center(60))
            else:
                print("\nAnda telah mencapai batas percobaan. Silakan coba beberapa saat lagi.".center(60))
    return False, None

## registrasi admin baru
def registrasi_admin():
    print("\n" + "="*60)
    print("Registrasi Admin Baru".center(60))
    print("="*60)

    # validasi username
    while True:
        print("\nUsername max. 12 karakter, harus kombinasi huruf dan angka, tidak boleh ada karakter khusus.".center(60))
        username = input("Username: ").strip().lower()
    
        username = username.replace(" ", "")

        if not username.isalnum() or len(username) > 12 or len(username) == 0:
            print("Format Username salah.".center(60))
            continue
        if username.isalpha() or username.isdigit():
            print("Username harus kombinasi huruf dan angka.")
            continue
        if username in admin_users:
            print("\nUsername sudah terdaftar. Silakan masukkan username lain.")
            # return False
            continue
    
        print("\nUsername valid.".center(60))
        break

    # validasi password
    while True:
        print("\nPassword harus minimal 8 karakter, memiliki huruf besar, kecil, angka dan simbol '!@#$%'".center(60))
        password = input("Password: ").strip()

        if len(password) < 8:
            print("Password minimal 8 karakter.")
            continue

        huruf_besar = 0
        huruf_kecil = 0
        angka = 0
        simbol = 0

        for i in password:
            if i >= 'A' and i <= 'Z':
                huruf_besar = huruf_besar + 1
            elif i >= 'a' and i <= 'z':
                huruf_kecil = huruf_kecil + 1
            elif i >= '0' and i <= '9':
                angka = angka + 1
            elif i == '!' or i == '@' or i == '#' or i == '$' or i == '%':
                simbol = simbol + 1

        if huruf_besar > 0 and huruf_kecil > 0 and angka > 0 and simbol > 0:
            print("\nPassword valid.")
            break
        else:
            print("Password harus kombinasi huruf besar, kecil, angka, dan simbol (!@#$%)")
            continue

    while True:
        nama = input("Nama: ").strip().capitalize()
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf.")
            continue
        break

    while True:
        role = input("Role (Admin/HR): ").strip().capitalize()
        if role not in ["Admin", "Hr"]:
            print("Role tidak valid. Pilih 'Admin' atau 'HR'.")
            continue
        if role == "Hr":
            role = "HR"
        break
    
    admin_users[username] = {
        "password": password,
        "nama": nama,
        "role": role
    }

    print("\nRegistrasi admin berhasil.".center(60))
    return True

            
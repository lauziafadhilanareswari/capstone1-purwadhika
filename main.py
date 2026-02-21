from authentication import login_admin, registrasi_admin
from employee_management import (
    tambah_karyawan, 
    lihat_semua_karyawan, 
    cari_karyawan, 
    edit_karyawan, 
    hapus_karyawan, 
    laporan_data_karyawan
) 
from payroll import menu_payroll
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print("\n" + "="*60)
    print("SISTEM MANAJEMEN KARYAWAN PERUSAHAAN".center(60))
    print("PT SUKSES SEJAHTERA AAMIIN".center(60))
    print("="*60)


## --- menu utama ---
def main_menu(user_data):
    while True:
        header()
        print(f"\nWelcome, {user_data['nama']} ({user_data['role']})".center(65))
        print("\n" + "="*60)
        print("\n----- Manajemen Karyawan -----")
        print("1. Tambah Karyawan Baru")
        print("2. Lihat Data Semua Karyawan")
        print("3. Cari Karyawan")
        print("4. Edit Data Karyawan")
        print("5. Hapus Data Karyawan")
        print("6. Laporan Data Karyawan")
        print("7. Payroll Karyawan")
        print("8. Logout")
        print("\n" + "-"*60)

        pilihan = input("\nPilih Menu (1-8): ").strip()

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            lihat_semua_karyawan()
        elif pilihan == "3":
            cari_karyawan()
        elif pilihan == "4":
            edit_karyawan()
        elif pilihan == "5":
            hapus_karyawan()
        elif pilihan == "6":
            laporan_data_karyawan()
        elif pilihan == "7":
            menu_payroll()
        elif pilihan == "8":
            print("\n" + "-"*60)
            print("Logout Berhasil".center(60))
            print("Terima Kasih".center(60))
            print("Telah Menggunakan Sistem Manajemen Karyawan.".center(60))
            print("="*60)
            menu_awal()
        else:
            print("Pilihan tidak valid. Silakan pilih 1-8.")
            input("Tekan enter untuk melanjutkan...")
    
    return True

## --- menu awal aplikasi ---
def menu_awal():
    while True:
        header()
        print("\n" + "-"*60)
        print("Login Sistem Manajemen Karyawan".center(60))
        print("-"*60)
        print("\n1. Login Sebagai Admin/HR")
        print("2. Registrasi Admin Baru")
        print("3. Keluar Aplikasi")
        print("-"*60)

        pilihan = input("Pilih Menu (1-3): ").strip()

        if pilihan == "1":
            sukses, user_data = login_admin()
            if sukses:
                main_menu(user_data)
        elif pilihan == "2":
            registrasi_admin()
        elif pilihan == "3":
            print("\n" + "="*60)
            print("Terima Kasih".center(60))
            print("="*60)
            # return False
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-3")


## --- fungsi utama program ---
def main():
    try:
        menu_awal()
    except KeyboardInterrupt:
        print("\n" + "="*60)
        print("Terima Kasih".center(60))
        print("="*60)


if __name__ == "__main__":
    main()
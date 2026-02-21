## CRUD karyawan

from employee_database import data_karyawan, get_karyawan_by_nip, get_karyawan_by_nama, get_karyawan_by_dept, get_karyawan_by_status
import datetime

## ---tabel data karyawan---
def tabel_data_karyawan(data=None):
    if data is None:
        data = data_karyawan
    
    if len(data) == 0:
        print("Tidak ada data karyawan.")
        return
    
    print("\n")
    print("="*115)
    print("TABEL DATA KARYAWAN".center(115))
    print("="*115)

    header = f"{'No':<3} | {'NIP':^5} | {'Nama':<20} | {'Jabatan':<15} | {'Departemen':<12} | {'Gaji':<15} | {'Status':<8} | {'Tgl Bergabung':<15}"
    print(header)
    print("-"*115)

    
    for i in range(len(data)):
        karyawan = data[i]
        No = i + 1
        gaji_format = f"Rp {karyawan['Gaji']:,}"
        print(f"{No:<4}| {karyawan['NIP']:^6}| {karyawan['Nama']:<20} | {karyawan['Jabatan']:<15} | {karyawan['Departemen']:<12} | {gaji_format:<15} | {karyawan['Status']:<8} | {karyawan['TanggalBergabung']:<15}")

    print("="*115)
    print(f"Total Karyawan: {len(data)}")
    print("="*115)

## ---tambah karyawan baru---
def tambah_karyawan():
    while True:
        print("\n" + "="*60)
        print("TAMBAH DATA KARYAWAN".center(60))
        print("="*60)

        # validasi NIP
        while True:
            nip = input("NIP (3 digit, contoh: 001): ").strip()
            
            if not nip.isdigit() or len(nip) != 3:
                print("NIP harus berupa 3 digit angka.")
                continue

            if get_karyawan_by_nip(nip):
                print("NIP sudah terdaftar. Gunakan NIP lain.")
                continue
            
            print("NIP valid.")
            break

        # validasi Nama
        while True:
            nama = input("Nama Lengkap: ").strip()

            if not nama.replace(" ", "").isalpha():                    
                print("Format Nama tidak valid")
                continue
            nama = nama.title()  
            print("Nama valid.")
            break

        # validasi Jabatan
        while True:
            jabatan = input("Jabatan: ").strip()

            if not jabatan.replace(" ", "").isalpha():
                print("Format Jabatan tidak valid")
                continue
            jabatan = jabatan.title()
            print("Jabatan valid.")
            break

        # validasi Dept
        while True:
            dept = input("Departemen: ").strip()

            if not dept.replace(" ", "").isalpha():
                print("Departemen harus berupa huruf.")
                continue
            dept = dept.title()
            print("Departemen valid.")
            break

        # validasi Gaji
        while True:
            gaji = input("Gaji (contoh: 5000000): ").strip()
            if gaji.isdigit():
                gaji = int(gaji)
                if gaji < 0:
                    print("Gaji tidak boleh negatif.")
                    continue
                else:
                    print("Gaji valid.")
                    break
            print("Format Gaji tidak valid.")

        # Status default
        status = "Aktif"

        # validasi Tanggal Bergabung
        while True:
            tgl = input("Tanggal Bergabung (contoh: 2026-01-01, tekan enter untuk tanggal sekarang): ").strip()

            if tgl == "":
                tgl = datetime.date.today().strftime("%Y-%m-%d")
                break

            try:
                datetime.datetime.strptime(tgl, "%Y-%m-%d")
                break
            except ValueError:
                print("Format tanggal harus YYYY-MM-DD.")

        print("\n" + "-"*60)
        print("Data yang akan ditambahkan:")
        print(f"NIP                 : {nip}")
        print(f"Nama                : {nama}")
        print(f"Jabatan             : {jabatan}")
        print(f"Departemen          : {dept}")
        print(f"Gaji                : {gaji}")
        print(f"Status              : {status}")
        print(f"Tanggal Bergabung   : {tgl}")

        ## validasi konfirmasi
        while True:
            konfirmasi = input("\nApakah data yg di input sudah benar? (y/n): ").strip().lower()

            if konfirmasi == 'y':
                data_karyawan.append({
                    "NIP": nip,
                    "Nama": nama,
                    "Jabatan": jabatan,
                    "Departemen": dept,
                    "Gaji": gaji,
                    "Status": status,
                    "TanggalBergabung": tgl
                })
            
                print("Data berhasil ditambahkan")
                tabel_data_karyawan(data_karyawan)
                break
            elif konfirmasi == 'n':
                print("Data telah dibatalkan.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih y/n.")
            
        if konfirmasi == 'n':
            continue

        while True:        
            lagi = input("\nIngin menambah karyawan lagi? (y/n): ").strip().lower()
            if lagi == 'y':
                break
            elif lagi == 'n':
                print("Kembali ke menu utama.")
                return
            else:
                print("Pilihan tidak valid. Silakan pilih y/n.")
            

## tampilan semua karyawan
def lihat_semua_karyawan():
    print("\n" + "="*60)
    print("DAFTAR SEMUA KARYAWAN: ")
    tabel_data_karyawan()

def cari_karyawan():
    while True:
        print("\n" + "="*60)
        print("PENCARIAN KARYAWAN".center(60))
        print("="*60)
        print("\n1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Departemen")
        print("4. Cari berdasarkan Status")
        print("0. Kembali")

        pilihan = input("\nPilih Menu (0-4): ").strip()
        hasil = []

        if pilihan == "1":
            nip = input("Masukkan NIP: ").strip()
            karyawan = get_karyawan_by_nip(nip)
            if karyawan:
                hasil = [karyawan]
            else:
                print(f"\nKaryawan dengan NIP '{nip}' tidak ditemukan.")
                print("\n1. Cari Ulang")
                print("2. Kembali >> Menu Utama")
                
                opsi = input("Pilih menu (1-2): ").strip()
                if opsi == "1":
                    continue
                else:
                    return
        
        elif pilihan == "2":
            nama = input("Masukkan Nama: ").strip()
            hasil = get_karyawan_by_nama(nama) or []
            if not hasil:
                print(f"\nKaryawan dengan nama '{nama}' tidak ditemukan.")
                print("\n1. Cari Ulang")
                print("2. Kembali >> Menu Utama")
                
                opsi = input("Pilih menu (1-2): ").strip()
                if opsi == "1":
                    continue
                else:
                    return

        elif pilihan == "3":
            dept = input("Departemen: ").strip()
            hasil = get_karyawan_by_dept(dept) or []
            if not hasil:
                print(f"\nKaryawan dengan departemen '{dept}' tidak ditemukan.")
                print("\n1. Cari Ulang")
                print("2. Kembali >> Menu Utama")
                
                opsi = input("Pilih menu (1-2): ").strip()
                if opsi == "1":
                    continue
                else:
                    return
        
        elif pilihan == "4":
            status = input("Status (Aktif/Non-Aktif): ").strip()
            if status.title() not in ["Aktif", "Non-Aktif"]:
                print("Status harus 'Aktif' atau 'Non-Aktif'.")
                continue
            hasil = get_karyawan_by_status(status)
            if not hasil:
                print(f"\nKaryawan dengan status '{status}' tidak ditemukan.")
                print("\n1. Cari Ulang")
                print("2. Kembali >> Menu Utama")
                
                opsi = input("Pilih menu (1-2): ").strip()
                if opsi == "1":
                    continue
                else:
                    return
        
        elif pilihan == "0":
            return True
        else:
            print("Pilihan tidak valid.")
            return True
    
        if hasil:
            print(f"Jumlah Karyawan: {len(hasil)}")
            tabel_data_karyawan(hasil)
        else:
            print("\nData tidak ditemukan.")
            print("\n1. Cari Ulang")
            print("2. Kembali >> Menu Utama")
            
            opsi = input("Pilih menu (1-2): ").strip()
            if opsi == "1":
                continue
            else:
                return

        while True:        
            lagi = input("\nIngin mencari karyawan lagi? (y/n): ").strip().lower()
            if lagi == 'y':
                break
            elif lagi == 'n':
                print("Kembali ke menu utama.")
                return
            else:
                print("Pilihan tidak valid. Silakan pilih y/n.")


## edit data karyawan
def edit_karyawan():
    print("\n" + "="*60)
    print("UBAH DATA KARYAWAN".center(60))
    print("="*60)

    while True:
        nip = input("Masukkan NIP Karyawan yang ingin di ubah: ").strip()

        if not nip.isdigit() or len(nip) != 3:
            print("NIP harus berupa 3 digit angka.")
            continue

        karyawan = get_karyawan_by_nip(nip)

        if not karyawan:
            print(f"\nKaryawan dengan NIP '{nip}' tidak ditemukan.")
            print("\n1. Coba NIP lain")
            print("0. Kembali ke menu utama")
            opsi = input("Pilih (0/1): ").strip()
            if opsi == "1":
                continue
            else:
                return
        break

    print("\nData karyawan:")
    tabel_data_karyawan([karyawan])

    while True:
        print("\nPilih data yang ingin di ubah:")
        print("1. Nama")
        print("2. Jabatan")
        print("3. Departemen")
        print("4. Gaji")
        print("5. Status (Aktif/Non-Aktif)")
        print("6. Tanggal Bergabung")
        print("0. Batal >>> Kembali")

        pilihan = input("\nPilih Menu (0-6): ").strip()

        if pilihan == "0":
            print("Ubah data dibatalkan.")
            return
        
        elif pilihan == "1":
            nama_baru = input("Masukkan Nama Karyawan Baru: ").strip().title()
            if nama_baru.replace(" ","").isalpha():
                karyawan["Nama"] = nama_baru
                print("\nNama berhasil diubah.")
            else:
                print("Nama harus berupa huruf.")
                continue

        elif pilihan == "2":
            jabatan_baru = input("Masukkan Jabatan baru: ").strip().title()
            if jabatan_baru.replace(" ", "").isalpha():
                karyawan["Jabatan"] = jabatan_baru
                print("\nJabatan berhasil diubah.")
            else:
                print("Jabatan tidak valid.")
                continue
            
        elif pilihan == "3":
            dept_baru = input("Masukkan Departemen baru: ").strip().title()
            if dept_baru.replace(" ", "").isalpha():
                karyawan["Departemen"] = dept_baru
                print("\nDepartemen berhasil diubah.")
            else:
                print("Departemen tidak valid.")
                continue
            
        elif pilihan == "4":
            gaji_baru = input("Masukkan Gaji baru: ").strip()
            if gaji_baru.isdigit():
                karyawan["Gaji"] = int(gaji_baru)
                print("\nGaji berhasil diubah.")
            else:
                print("Gaji tidak valid.")
                continue
            
        elif pilihan == "5":
            status_baru = input("Masukkan Status baru (Aktif/Non-Aktif): ").strip().title()
            if status_baru in ["Aktif", "Non-Aktif"]:
                karyawan["Status"] = status_baru
                print("\nStatus berhasil diubah.")
            else:
                print("Status tidak valid.")
                continue
            
        elif pilihan == "6":
            tgl_baru = input("Masukkan Tanggal Bergabung baru (YYYY-MM-DD): ").strip()
            try:
                datetime.datetime.strptime(tgl_baru, "%Y-%m-%d")
                karyawan["TanggalBergabung"] = tgl_baru
                print("\nTanggal bergabung berhasil diubah")
            except ValueError:
                print("Format tanggal salah")
                continue
            
        else:
            print("\nPilihan tidak valid")
            continue
        
        print("\nData setelah diubah:")
        tabel_data_karyawan([karyawan])
        
        while True:        
            lagi = input("\nIngin mengubah data karyawan lagi? (y/n): ").strip().lower()
            if lagi == 'y':
                break
            elif lagi == 'n':
                print("Kembali ke menu utama.")
                return
            else:
                print("Pilihan tidak valid. Silakan pilih y/n.")
                continue


## hapus data karyawan        
def hapus_karyawan():
    print("\n" + "="*60)
    print("HAPUS DATA KARYAWAN".center(60))
    print("="*60)
    
    while True:
        nip = input("\nMasukkan NIP karyawan yang ingin dihapus: ").strip()

        if not nip.isdigit() or len(nip) != 3:
            print("NIP harus berupa 3 digit angka.")
            continue

        karyawan = get_karyawan_by_nip(nip)

        if not karyawan:
            print("NIP tidak ditemukan.")
            coba_lagi = input("\nIngin coba NIP lain? (y/n): ").strip().lower()
            if coba_lagi == 'y':
                continue
            else:
                print("Kembali >> Menu Utama")
                return

        print("\nData karyawan ditemukan:")
        tabel_data_karyawan([karyawan])
                
        
        while True:
            konfirmasi = input("\nApakah Anda yakin ingin menghapus data ini? (y/n): ").strip().lower()

            if konfirmasi == "y":
                data_karyawan.remove(karyawan)
                print("\nData karyawan berhasil dihapus.")
                break
            elif konfirmasi == "n":
                print("Penghapusan dibatalkan.")
                continue
            else:
                print("Pilihan tidak valid. Masukkan y atau n.")
                continue
    

        while True:        
            lagi = input("\nIngin menghapus karyawan lagi? (y/n): ").strip().lower()
            if lagi == 'y':
                break
            elif lagi == 'n':
                print("Kembali ke menu utama.")
                return
            else:
                print("Pilihan tidak valid. Silakan pilih y/n.")
                continue


## laporan ringkasan karyawan
def laporan_data_karyawan():
    print("\n" + "="*60)
    print("LAPORAN DATA KARYAWAN".center(60))
    print("="*60)
    
    total = len(data_karyawan)
    aktif = len([karyawan for karyawan in data_karyawan if karyawan['Status'] == 'Aktif'])
    non_aktif = total - aktif
    
    # Hitung per departemen
    dept_count = {}
    for karyawan in data_karyawan:
        dept = karyawan['Departemen']
        dept_count[dept] = dept_count.get(dept, 0) + 1

    # perhitungan total gaji
    total_gaji = sum(karyawan['Gaji'] for karyawan in data_karyawan)
    rata_gaji = total_gaji // total if total > 0 else 0
    
    print(f"\nTotal Karyawan       : {total}")
    print(f"Karyawan Aktif       : {aktif}")
    print(f"Karyawan Non-Aktif   : {non_aktif}")
    print(f"\nTotal Gaji Bulanan   : Rp {total_gaji:,}")
    print(f"Rata-rata Gaji       : Rp {rata_gaji:,}")
    
    print("\n" + "-"*60)
    print("DISTRIBUSI PER DEPARTEMEN:")
    print("-"*60)
    for dept, count in dept_count.items():
        print(f"{dept:<20} : {count} orang")
    
    print("-"*60)
    print("\nDETAIL LENGKAP:")
    tabel_data_karyawan()



        
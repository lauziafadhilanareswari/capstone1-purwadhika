## Demo Script Sistem Manajemen Karyawan Perusahaan PT SUKSES SEJAHTERA AAMIIN

from employee_database import data_karyawan, data_lembur
from employee_management import tabel_data_karyawan
from payroll import hitung_gaji_bersih
import datetime


# menampilkan semua karyawan dahulu
def demo_display_all():
    print("\n" + "="*60)
    print("DAFTAR SEMUA KARYAWAN".center(60))
    print("="*60)
    tabel_data_karyawan()

# menampilkan pencarian karyawan
def demo_search():
    print("\n" + "="*60)
    print("PENCARIAN KARYAWAN".center(60))
    print("="*60)

    from employee_database import get_karyawan_by_dept, get_karyawan_by_nama, get_karyawan_by_nip, get_karyawan_by_status, get_karyawan_by_jabatan

    print("\n1. Cari karyawan di departemen 'IT':")
    it_employees = get_karyawan_by_dept('IT')
    tabel_data_karyawan(it_employees)
    
    print("\n2. Cari karyawan dengan nama mengandung 'Budi':")
    budi_employees = get_karyawan_by_nama('Budi')
    tabel_data_karyawan(budi_employees)
    
    print("\n3. Cari karyawan dengan NIP '001':")
    nip_employees = get_karyawan_by_nip('001')
    tabel_data_karyawan(nip_employees)
    
    print("\n4. Cari karyawan dengan status aktif:")
    aktif_employees = get_karyawan_by_status('Aktif')
    tabel_data_karyawan(aktif_employees)
    
    print("\n5. Cari karyawan dengan jabatan 'Manager':")
    manager_employees = get_karyawan_by_jabatan('Manager')
    tabel_data_karyawan(manager_employees)

## menambah karyawan baru
def demo_add_employee():
    print("\n" + "="*60)
    print("MENAMBAH KARYAWAN BARU".center(60))
    print("="*60)
    
    # Data karyawan baru untuk demo
    new_employee = {
        "NIP": "007",
        "Nama": "James Bond",
        "Jabatan": "Agent",
        "Dept": "Security",
        "Gaji": 15000000,
        "Status": "Aktif",
        "TanggalBergabung": "2026-02-01"
    }
    
    print("\nData karyawan yang akan ditambahkan:")
    print(f"NIP              : {new_employee['NIP']}")
    print(f"Nama             : {new_employee['Nama']}")
    print(f"Jabatan          : {new_employee['Jabatan']}")
    print(f"Departemen       : {new_employee['Dept']}")
    print(f"Gaji             : Rp {new_employee['Gaji']:,}")
    print(f"Status           : {new_employee['Status']}")
    print(f"Tanggal Bergabung: {new_employee['TanggalBergabung']}")
    
    # Tambahkan ke database (untuk demo)
    data_karyawan.append(new_employee)
    
    print("\n✓ Karyawan berhasil ditambahkan!")
    print("\nData setelah penambahan:")
    tabel_data_karyawan([new_employee])

## perhitungan payroll
def demo_payroll():
    print("\n" + "="*60)
    print("PERHITUNGAN PAYROLL".center(60))
    print("="*60)
    
    # Simulasi data lembur untuk demo
    print("\n1. Simulasi input lembur untuk NIP 001:")
    demo_lembur = {
        "NIP": "001",
        "Nama": "Budi Santoso",
        "TanggalLembur": datetime.date.today().strftime("%Y-%m-%d"),
        "JamLembur": 10.0,
        "Keterangan": "Project deadline"
    }
    data_lembur.append(demo_lembur)
    
    print(f"   NIP       : {demo_lembur['NIP']}")
    print(f"   Nama      : {demo_lembur['Nama']}")
    print(f"   Tanggal   : {demo_lembur['TanggalLembur']}")
    print(f"   Jam Lembur: {demo_lembur['JamLembur']}")
    print(f"   Keterangan: {demo_lembur['Keterangan']}")
    
    print("\n2. Perhitungan slip gaji untuk NIP 001:")
    
    from employee_database import get_karyawan_by_nip
    karyawan = get_karyawan_by_nip("001")
    
    if karyawan:
        hasil = hitung_gaji_bersih(karyawan['Gaji'], 10.0)
        
        print("\n" + "-"*60)
        print(f"SLIP GAJI - {karyawan['Nama'].upper()}".center(60))
        print("-"*60)
        print(f"NIP               : {karyawan['NIP']}")
        print(f"Nama              : {karyawan['Nama']}")
        print(f"Jabatan           : {karyawan['Jabatan']}")
        print(f"Departemen        : {karyawan['Dept']}")
        print(f"Periode           : {datetime.date.today().strftime('%Y-%m')}")
        print("-"*60)
        print(f"Gaji Pokok        : Rp {hasil['gaji_pokok']:>15,}")
        print(f"Uang Lembur (10 jam): Rp {hasil['uang_lembur']:>15,.0f}")
        print("-"*60)
        print(f"Gaji Kotor        : Rp {hasil['gaji_kotor']:>15,.0f}")
        print(f"Pajak (5%)        : Rp {hasil['potongan_pajak']:>15,.0f}")
        print("="*60)
        print(f"GAJI BERSIH       : Rp {hasil['gaji_bersih']:>15,.0f}")
        print("="*60)


## Statistik dan laporan
def demo_statistics():
    
    print("\n" + "="*60)
    print("STATISTIK & LAPORAN".center(60))
    print("="*60)
    
    total = len(data_karyawan)
    aktif = len([karyawan for karyawan in data_karyawan if karyawan['Status'] == 'Aktif'])
    
    # Hitung per departemen
    dept_count = {}
    for karyawan in data_karyawan:
        dept = karyawan['Dept']
        dept_count[dept] = dept_count.get(dept, 0) + 1
    
    # Hitung total gaji
    total_gaji = sum(karyawan['Gaji'] for karyawan in data_karyawan)
    rata_gaji = total_gaji // total if total > 0 else 0
    
    print(f"\nTotal Karyawan       : {total}")
    print(f"Karyawan Aktif       : {aktif}")
    print(f"Karyawan Non-Aktif   : {total - aktif}")
    print(f"\nTotal Gaji Bulanan   : Rp {total_gaji:,}")
    print(f"Rata-rata Gaji       : Rp {rata_gaji:,}")
    
    print("\n" + "-"*60)
    print("DISTRIBUSI PER DEPARTEMEN:")
    print("-"*60)
    for dept, count in dept_count.items():
        print(f"{dept:<20} : {count} orang")


### --- menjalankan semua demo ---
def run_all_demos():

    print("\n" + "="*60)
    print("SISTEM MANAJEMEN KARYAWAN".center(60))
    print("="*60)
    
    input("\nTekan Enter untuk Demo 1: Menampilkan Semua Karyawan...")
    demo_display_all()
    
    input("\nTekan Enter untuk Demo 2: Pencarian Karyawan...")
    demo_search()
    
    input("\nTekan Enter untuk Demo 3: Menambah Karyawan Baru...")
    demo_add_employee()
    
    input("\nTekan Enter untuk Demo 4: Perhitungan Payroll...")
    demo_payroll()
    
    input("\nTekan Enter untuk Demo 5: Statistik & Laporan...")
    demo_statistics()
    
    print("\n" + "="*60)
    print("SELESAI".center(60))
    print("="*60)

if __name__ == "__main__":
    run_all_demos()


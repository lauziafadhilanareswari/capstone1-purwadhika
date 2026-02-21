from employee_database import data_karyawan, data_lembur, get_karyawan_by_nip
import datetime


def hitung_gaji_bersih(gaji_pokok, jam_lembur=0):
    pajak = 0.05 ## pajak 5%

    # tarif lembur per jam (1.5x gaji per jam)
    gaji_per_jam = gaji_pokok / 160 # asumsi 160 jam kerja per bulan
    uang_lembur = jam_lembur * gaji_per_jam * 1.5

    gaji_kotor = gaji_pokok + uang_lembur
    potongan_pajak = gaji_kotor * pajak

    gaji_bersih = gaji_kotor - potongan_pajak

    return {
        "gaji_pokok": gaji_pokok,
        "uang_lembur": uang_lembur,
        "gaji_kotor": gaji_kotor,
        "potongan_pajak": potongan_pajak,
        "gaji_bersih": gaji_bersih
    }

def input_lembur():
    print("\n" + "="*60)
    print("INPUT DATA LEMBUR".center(60))
    print("="*60)

    while True:
        nip = input("\nMasukkan NIP Karyawan (3 digit angka, contoh: 003): ").strip()

        if not nip.isdigit() or len(nip) != 3:
            print("NIP harus berupa 3 digit angka.")
            continue
        
        karyawan = get_karyawan_by_nip(nip)

        if not karyawan:
            print(f"\nKaryawan dengan NIP '{nip}' tidak ditemukan.")
            coba_lagi = input("Ingin coba NIP lain? (y/n): ").strip().lower()
            if coba_lagi == 'y':
                continue
            else:
                print("Kembali ke menu payroll.")
                return
        
        break
        
    print(f"\nNama Karyawan: {karyawan['Nama']}")
    print(f"Jabatan : {karyawan['Jabatan']}")
    print(f"Departemen: {karyawan['Departemen']}")

    ## input utk jam lembur
    while True:
        jam_lembur = input("\nMasukkan jumlah jam lembur: ").strip()

        if jam_lembur.replace(".", "").isdigit():
            jam_lembur = float(jam_lembur)
            if jam_lembur >= 0:
                break
        print("Format jam lembur salah (misal: 2.5). Silakan coba lagi.")

    ## input utk tgl lembur
    while True:
        tgl = input("\nMasukkan tanggal lembur (YYYY-MM-DD, tekan Enter untuk hari ini): ").strip()
        if tgl == "":
            tgl = datetime.date.today().strftime("%Y-%m-%d")
            break
        
        try:
            datetime.datetime.strptime(tgl, "%Y-%m-%d")
            break
        except:
            print("Format tanggal salah (YYYY-MM-DD).")

    keterangan = input("Keterangan (Opsional): ").strip()

    ## simpan data lembur
    data_lembur.append({
        "NIP": nip,
        "Nama": karyawan['Nama'],
        "TanggalLembur": tgl,
        "JamLembur": jam_lembur,
        "Keterangan": keterangan
    })
    print("Data lembur berhasil disimpan.")

def lihat_data_lembur():
    if len(data_lembur) == 0:
        print("Tidak ada data lembur.")
        return

    print("\n" + "="*90)
    print("Data Lembur Karyawan".center(90))
    print("="*90)

    header = f"{'No':<4} | {'NIP':<6} | {'Nama':<20} | {'Tanggal':<12} | {'Jam':<6} | {'Keterangan':<25}"
    print(header)
    print("-"*90)
    
    for i in range(len(data_lembur)):
        lembur = data_lembur[i]
        print(f"{i+1:<4} | {lembur['NIP']:<6} | {lembur['Nama']:<20} | {lembur['TanggalLembur']:<12} | {lembur['JamLembur']:<6.1f} | {lembur['Keterangan']:<25}")
    
    print("="*90)


### --- Menghitung dan menampilkan payroll karyawan ---
def hitung_payroll():

    print("\n" + "="*60)
    print("PERHITUNGAN PAYROLL".center(60))
    print("="*60)
    
    print("\n1. Hitung payroll satu karyawan")
    print("2. Hitung payroll semua karyawan")
    print("0. Kembali")
    
    pilihan = input("\nPilih menu (0-2): ").strip()
    
    if pilihan == "1":
        while True:
            nip = input("\nMasukkan NIP karyawan: ").strip()

            
            if not nip.isdigit() or len(nip) != 3:
                print("NIP harus berupa 3 digit angka.")
                continue
            karyawan = get_karyawan_by_nip(nip)
        
            if not karyawan:
                print(f"\nKaryawan dengan NIP '{nip}' tidak ditemukan.")
                coba_lagi = input("Ingin coba NIP lain? (y/n): ").strip().lower()
                if coba_lagi == 'y':
                    continue
                else:
                    return
        
            # Hitung total jam lembur bulan ini
            bulan_ini = datetime.date.today().strftime("%Y-%m")
            total_lembur = sum(
                lembur['JamLembur'] 
                for lembur in data_lembur 
                if lembur['NIP'] == nip and lembur['TanggalLembur'].startswith(bulan_ini)
            )
            
            hasil = hitung_gaji_bersih(karyawan['Gaji'], total_lembur)
            
            print("\n" + "="*60)
            print(f"SLIP GAJI - {karyawan['Nama'].upper()}".center(60))
            print("="*60)
            print(f"NIP               : {karyawan['NIP']}")
            print(f"Nama              : {karyawan['Nama']}")
            print(f"Jabatan           : {karyawan['Jabatan']}")
            print(f"Departemen        : {karyawan['Departemen']}")
            print(f"Periode           : {bulan_ini}")
            print("-"*60)
            print(f"Gaji Pokok        : Rp {hasil['gaji_pokok']:>15,}")
            print(f"Uang Lembur ({total_lembur:.1f} jam): Rp {hasil['uang_lembur']:>15,.0f}")
            print("-"*60)
            print(f"Gaji Kotor        : Rp {hasil['gaji_kotor']:>15,.0f}")
            print(f"Pajak (5%)        : Rp {hasil['potongan_pajak']:>15,.0f}")
            print("="*60)
            print(f"GAJI BERSIH       : Rp {hasil['gaji_bersih']:>15,.0f}")
            print("="*60)

            while True:        
                lagi = input("\nIngin hitung payroll karyawan lain? (y/n): ").strip().lower()
                if lagi == 'y':
                    break
                elif lagi == 'n':
                    print("Kembali ke menu payroll.")
                    return
                else:
                    print("Pilihan tidak valid. Silakan pilih y/n.")
            
    elif pilihan == "2":
        print("\n" + "="*125)
        print("PAYROLL SEMUA KARYAWAN".center(125))
        print("="*125)
        
        bulan_ini = datetime.date.today().strftime("%Y-%m")
        print(f"Periode: {bulan_ini}")
        print("-"*125)
        
        header = f"{'No':<3} | {'NIP':<6} | {'Nama':<20} | {'Departemen':<10} | {'Gaji Pokok':<14} | {'Lembur':<14} | {'Pajak':<14} | {'Gaji Bersih':<14}"
        print(header)
        print("-"*125)
        
        total_payroll = 0
        
        for i in range(len(data_karyawan)):
            karyawan = data_karyawan[i]
            jam_lembur = 0
        
            # hitung jam lembur
            for lembur in data_lembur:
                if lembur['NIP'] == karyawan['NIP'] and lembur['TanggalLembur'].startswith(bulan_ini):
                    jam_lembur += lembur['JamLembur']
            
            hasil = hitung_gaji_bersih(karyawan['Gaji'], jam_lembur)
            total_payroll += hasil['gaji_bersih']
            
            print(f"{i+1:<3} | {karyawan['NIP']:<6} | {karyawan['Nama']:<20} | {karyawan['Departemen']:<10} | Rp {karyawan['Gaji']:>10,} | Rp {hasil['uang_lembur']:>10,.0f} | Rp {hasil['potongan_pajak']:>10,.0f} | Rp {hasil['gaji_bersih']:>10,.0f}")
        
        print("="*125)
        print(f"TOTAL PAYROLL BULANAN: Rp {total_payroll:,}".rjust(125))
        print("="*125)


### --- Menu utama payroll management ---
def menu_payroll():
    while True:
        print("\n" + "="*60)
        print("PAYROLL MANAGEMENT".center(60))
        print("="*60)
        print("\n1. Input Data Lembur")
        print("2. Lihat Data Lembur")
        print("3. Hitung Payroll")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("\nPilih menu (0-3): ").strip()
        
        if pilihan == "1":
            input_lembur()
        elif pilihan == "2":
            lihat_data_lembur()
        elif pilihan == "3":
            hitung_payroll()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Pilih 0-3.")

## database karyawan

data_karyawan = [
    {
        "NIP": "001", 
        "Nama": "Budi Santoso", 
        "Jabatan": "Manager", 
        "Departemen": "IT", 
        "Gaji": 10000000,
        "Status": "Aktif",
        "TanggalBergabung": "2020-01-15"
    },
    {
        "NIP": "002", 
        "Nama": "Marissa Caca", 
        "Jabatan": "Staff", 
        "Departemen": "Marketing", 
        "Gaji": 5000000,
        "Status": "Aktif",
        "TanggalBergabung": "2021-03-20"
    },
    {
        "NIP": "003", 
        "Nama": "Cici Lestari", 
        "Jabatan": "Staff", 
        "Departemen": "Marketing",
        "Gaji": 5000000,
        "Status": "Aktif",
        "TanggalBergabung": "2021-06-10"
    },
    {
        "NIP": "004", 
        "Nama": "Dedi Kurniawan", 
        "Jabatan": "Supervisor", 
        "Departemen": "Marketing", 
        "Gaji": 8000000,
        "Status": "Aktif",
        "TanggalBergabung": "2019-11-05"
    },
    {
        "NIP": "005", 
        "Nama": "Eka Pratama", 
        "Jabatan": "Staff", 
        "Departemen": "IT", 
        "Gaji": 6000000,
        "Status": "Aktif",
        "TanggalBergabung": "2022-02-14"
    },
    {
        "NIP": "006", 
        "Nama": "Syifa Rahma", 
        "Jabatan": "Staff", 
        "Departemen": "Finance", 
        "Gaji": 5500000,
        "Status": "Aktif",
        "TanggalBergabung": "2022-05-18"
    }
]

data_lembur = []

def get_karyawan_by_nip(nip):
    for karyawan in data_karyawan:
        if karyawan["NIP"] == nip:
            return karyawan
    return None

def get_karyawan_by_nama(nama):
    hasil = []
    nama_lower = nama.lower()
    for karyawan in data_karyawan:
        if nama_lower in karyawan["Nama"].lower():
            hasil.append(karyawan)
    return hasil

def get_karyawan_by_dept(dept):
    hasil = []
    for karyawan in data_karyawan:
        if karyawan["Departemen"].lower() == dept.lower():
            hasil.append(karyawan)
    return hasil

def get_karyawan_by_jabatan(jabatan):
    hasil = []
    for karyawan in data_karyawan:
        if karyawan["Jabatan"].lower() == jabatan.lower():
            hasil.append(karyawan)
    return hasil

def get_karyawan_by_status(status):
    hasil = []
    for karyawan in data_karyawan:
        if karyawan["Status"].lower() == status.lower():
            hasil.append(karyawan)
    return hasil















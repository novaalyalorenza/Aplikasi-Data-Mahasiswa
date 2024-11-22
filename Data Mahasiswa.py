mahasiswa = {}

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))

    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
    print("Data berhasil ditambahkan!")

def ubah_data():
    nim = input("Masukkan NIM yang ingin diubah: ")
    if nim in mahasiswa:
        nama = input("Masukkan Nama baru (kosongkan jika tidak ingin diubah): ")
        tugas = input("Masukkan Nilai Tugas baru (kosongkan jika tidak ingin diubah): ")
        uts = input("Masukkan Nilai UTS baru (kosongkan jika tidak ingin diubah): ")
        uas = input("Masukkan Nilai UAS baru (kosongkan jika tidak ingin diubah): ")

        if nama:
            mahasiswa[nim]['nama'] = nama
        if tugas:
            mahasiswa[nim]['tugas'] = float(tugas)
        if uts:
            mahasiswa[nim]['uts'] = float(uts)
        if uas:
            mahasiswa[nim]['uas'] = float(uas)

        mahasiswa[nim]['nilai_akhir'] = 0.3 * mahasiswa[nim]['tugas'] + 0.35 * mahasiswa[nim]['uts'] + 0.35 * mahasiswa[nim]['uas']
        print("Data berhasil diubah!")
    else:
        print("NIM tidak ditemukan!")

def hapus_data():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("NIM tidak ditemukan!")

def tampilkan_data():
    if not mahasiswa:
        print("Data mahasiswa masih kosong.")
    else:
        print("=====================================================================================")
        print("|   NIM     |            Nama            |  Tugas  |  UTS  |  UAS  |   Nilai Akhir  |")
        print("=====================================================================================")
        for nim, data in mahasiswa.items():
            print(f"| {nim:4} | {data['nama']:10} | {data['tugas']:5.2f} | {data['uts']:4.2f} | {data['uas']:4.2f} | {data['nilai_akhir']:9.2f} |")
        print("=====================================================================================")

def cari_data():
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print(f"Nama: {data['nama']}")
        print(f"Nilai Tugas: {data['tugas']}")
        print(f"Nilai UTS: {data['uts']}")
        print(f"Nilai UAS: {data['uas']}")
        print(f"Nilai Akhir: {data['nilai_akhir']}")
    else:
        print("NIM tidak ditemukan!")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '0':
        break
    else:
        print("Pilihan tidak valid!")
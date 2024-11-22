# Aplikasi-Data-Mahasiswa

### Penjelasan Kode
Kode Python ini adalah program pengelolaan data mahasiswa sederhana.
Program ini menggunakan dictionary untuk menyimpan data mahasiswa, dan
menyediakan fitur CRUD (Create, Read, Update, Delete). Berikut adalah
penjelasan detail untuk setiap fungsi:

#### 1. Fungsi tambah_data()
**Tujuan:** Menambahkan data mahasiswa ke dalam dictionary.
**Proses:**
1. Mengambil input NIM, Nama, Nilai Tugas, UTS, dan UAS dari pengguna.
2. Menghitung nilai akhir menggunakan formula:
 Nilai Akhir = 30% x Tugas + 35% x UTS + 35% x UAS
3. Menyimpan data ke dalam dictionary dengan struktur berikut:
 mahasiswa[NIM] = {'nama': Nama, 'tugas': Tugas, 'uts': UTS, 'uas': UAS,
'nilai_akhir': NilaiAkhir}
**Contoh Struktur Data:**
mahasiswa = {
 '12345': {'nama': 'Andi', 'tugas': 80, 'uts': 85, 'uas': 90, 'nilai_akhir': 86.5}
}

#### 2. Fungsi ubah_data()
**Tujuan:** Mengubah data mahasiswa berdasarkan NIM.
**Proses:**
1. Memeriksa apakah NIM ada dalam dictionary.
2. Meminta input baru untuk setiap atribut (Nama, Tugas, UTS, UAS).
3. Jika input tidak kosong, data di-update.
4. Menghitung kembali nilai akhir berdasarkan nilai terbaru.
   
#### 3. Fungsi hapus_data()
**Tujuan:** Menghapus data mahasiswa berdasarkan NIM.
**Proses:**
1. Memeriksa apakah NIM ada dalam dictionary.
2. Jika ada, data mahasiswa dihapus menggunakan del.
   
#### 4. Fungsi tampilkan_data()
**Tujuan:** Menampilkan semua data mahasiswa dalam bentuk tabel.
**Proses:**
1. Memeriksa apakah dictionary mahasiswa kosong.
2. Jika ada data, semua data ditampilkan dalam format tabel menggunakan
string formatting.

#### 5. Fungsi cari_data()
**Tujuan:** Mencari data mahasiswa berdasarkan NIM.
**Proses:**
1. Memeriksa apakah NIM ada dalam dictionary.
2. Jika ada, menampilkan informasi lengkap mahasiswa tersebut.
   
#### 6. Loop Menu
Program berjalan dalam loop untuk menampilkan menu pilihan kepada
pengguna. Pengguna dapat memilih fitur berdasarkan input angka (1-5 untuk
fungsi, 0 untuk keluar).
#### Catatan Tambahan
- Data disimpan hanya dalam memori, sehingga akan hilang saat program
ditutup.
- Untuk penyimpanan permanen, data dapat disimpan ke file menggunakan
modul seperti pickle atau JSON.

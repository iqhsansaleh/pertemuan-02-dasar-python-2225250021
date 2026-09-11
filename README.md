# pertemuan-02-dasar-python-2225250021
# Profil Saya

## 🧑‍💻 Biodata Mahasiswa
- **Nama:** Iqhsan Saleh
- **NIM:** 2225250021
- **Kelas:** 3A

---

## 🎯 Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas mata kuliah Algoritma dan Pemrograman. Program ini bertujuan untuk mengetahui Dasar Python di VS Code dan Pengumpulan melalui GitHub.

---

## 📂 Daftar dan Fungsi Berkas
* `.gitignore`: Berkas konfigurasi untuk mengabaikan berkas atau folder yang tidak perlu diunggah ke repositori GitHub.
* `README.md`: Berkas dokumentasi utama yang berisi panduan dan informasi mengenai proyek ini.
* `latihan/`: Folder yang berisi berkas-berkas kode latihan dasar pemrograman Python.
  * `01_biodata.py`: Program latihan untuk menampilkan identitas dan biodata diri.
  * `02_persegi_panjang.py`: Program latihan untuk menghitung luas dan keliling persegi panjang.
  * `03_konversi_suhu.py`: Program latihan untuk mengonversi nilai suhu antar skala (Celcius, Fahrenheit, dll).
  * `04_nilai_akhir.py`: Program latihan untuk menghitung nilai akhir mahasiswa berdasarkan komponen bobot nilai.
* `tugas/`: Folder yang berisi berkas kode tugas utama praktikum.
  * `kalkulator_koordinat.py`: Program utama untuk menghitung jarak Euclidean dan titik tengah antara dua koordinat.

---

## 💻 Cara Menjalankan Program di VS Code

### Cara 1: Menggunakan Terminal Terintegrasi VS Code (Rekomendasi)
1. Buka folder `pertemuan-02-dasar-python-NIM` menggunakan VS Code.
2. Buka Terminal di VS Code dengan menekan tombol kombinasi `Ctrl + ~` (atau klik menu **Terminal** > **New Terminal**).
3. Untuk menjalankan **Tugas Utama**, ketik perintah berikut di terminal lalu tekan Enter:
   ```bash
   python tugas/kalkulator_koordinat.py
   ```
4. Untuk menjalankan salah satu berkas **Latihan**, gunakan perintah:
   ```bash
   python latihan/01_biodata.py
   ```

### Cara 2: Menggunakan Tombol Run (GUI)
1. Buka berkas kode yang ingin dijalankan (misalnya: `kalkulator_koordinat.py`) di VS Code.
2. Pastikan ekstensi **Python** dari Microsoft sudah terinstal di VS Code Anda.
3. Klik tombol **Play (Run Python File)** ▷ yang berada di pojok kanan atas jendela editor VS Code.

---

## 🧪 Hasil Uji Coba (*Test Case*)
Berikut adalah tabel hasil pengujian program menggunakan tiga skenario *test case* wajib untuk menghitung jarak dan titik tengah antara koordinat A dan B:

| Kasus | Input Koordinat A | Input Koordinat B | Ekspektasi Jarak | Ekspektasi Titik Tengah | Status |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | `(0, 0)` | `(3, 4)` | 5.00 | `(1.50, 2.00)` | ✅ Sukses |
| **2** | `(-2, 1)` | `(4, 1)` | 6.00 | `(1.00, 1.00)` | ✅ Sukses |
| **3** | `(2.5, -1)` | `(2.5, 3)` | 4.00 | `(2.50, 1.00)` | ✅ Sukses

---

## 📝 Refleksi Singkat & Sumber

### Refleksi
* **Konsep yang paling saya pahami adalah** implementasi rumus matematika ke dalam kode Python di VS Code (seperti fungsi `math.sqrt`) **karena** langkah-langkah logika perhitungannya sangat jelas dan linier sesuai dengan rumus geometri dasar.
* **Kesalahan yang saya temukan adalah** terjadinya *error* tipe data saat mencoba menghitung koordinat berupa angka desimal (float) **dan saya memperbaikinya dengan** mengubah fungsi input yang semula menggunakan `int()` menjadi `float()` agar program dapat menerima semua jenis angka.
* **Pada pertemuan berikutnya saya ingin lebih memahami** struktur percabangan (kondisional) dan perulangan yang lebih kompleks agar bisa membuat program dengan validasi input yang lebih ketat.


### Sumber yang Digunakan
1. **Visual Studio Code** - Lingkungan pengembangan terintegrasi (IDE) yang digunakan untuk penulisan, penyuntingan, dan pengujian kode program.
2. **Fasilitas Perangkat Keras (Laptop Non-Pribadi)** - Menggunakan komputer/laptop fasilitas bersama (Lab Kampus/Perpustakaan/Pinjaman) sebagai infrastruktur penunjang pengerjaan tugas selama praktikum berlangsung.
3. **Buku Pengantar Algoritma dan Pemrograman** - Buku referensi utama untuk memahami konsep dasar logika pemrograman, struktur runtunan, dan implementasi kode menggunakan Python.


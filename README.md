# 📚 E-Book & Modul Ajar AI Generator (SD Kurikulum Merdeka)

Aplikasi web cerdas berbasis **Node.js & Google Gemini AI** untuk menyusun dan menghasilkan **Buku Siswa & Modul Ajar Sekolah Dasar (SD)** siap cetak format A4 dalam hitungan detik. 

Didesain khusus untuk memenuhi standar resmi **Capaian Pembelajaran (CP) No. 020 Tahun 2026** (Kurikulum Merdeka) serta siap dipasarkan sebagai produk digital premium di platform seperti **Lynk.id**.

---

## 🌟 Fitur Unggulan

### 1. 📖 Pemetaan Kurikulum & Ekstraksi Dokumen Referensi
* **Dukungan Dokumen Pengguna**: Unggah file silabus atau materi acuan dalam format `.pdf`, `.docx`, atau `.txt`. Sistem AI akan mengekstrak dan mengikuti struktur bab serta materi dari file tersebut secara presisi.
* **Standar Capaian Pembelajaran (CP) Otomatis**: Jika tidak mengunggah dokumen, sistem otomatis mengacu pada **CP No. 020 Tahun 2026** per Fase dan Kelas:
  * **Fase A (Kelas 1 & 2 SD)**
  * **Fase B (Kelas 3 & 4 SD)**
  * **Fase C (Kelas 5 & 6 SD)**

### 2. 🎨 Sampul Tematik Eksklusif per Tingkat Kelas (Kelas 1–6)
* Setiap jenjang kelas memiliki tema warna gradien, badge fase, dan ilustrasi sampul 3D bergaya animasi Pixar yang unik:
  * **Kelas 1**: Hijau Zamrud (*Dasar Keislaman & Hijaiah Tunggal*)
  * **Kelas 2**: Biru Langit (*Hijaiah Bersambung & Ibadah*)
  * **Kelas 3**: Ungu Lembut (*Shalat, Zikir, & Sifat Terpuji*)
  * **Kelas 4**: Oranye Cerah (*Tanda Baligh & Akhlak Mulia*)
  * **Kelas 5**: Hijau Segar (*Toleransi, Zakat, & Ukhuwah*)
  * **Kelas 6**: Magenta Elegan (*Iman Hari Akhir & Kepemimpinan*)

### 3. 📐 Tata Letak Simetris & Sistem 2-Halaman per Bab (Bebas Halaman Kosong)
Struktur layout dirancang pas dengan dimensi fisik **A4 Portrait (210 x 297 mm)** tanpa risiko teks meluber:
* **Halaman 1 (Observasi & Materi Utama)**:
  * Header Bab & Indikator Capaian Pembelajaran.
  * Kartu Ilustrasi Utama (*Hero Banner 3D*) simetris di tengah halaman dengan teks observasi *Ayo Mengamati*.
  * Penjelasan Sub-Bab A dengan tipografi terjustifikasi yang rapi.
* **Halaman 2 (Pendalaman, Karakter, & Asesmen Formatif)**:
  * Penjelasan Sub-Bab B & Penerapan Praktis.
  * **📖 Kamus Cilik**: Kotak kosakata baru 2 kolom.
  * **🌟 Mutiara Hikmah**: Kisah teladan inspiratif.
  * **🎉 Aktivitas Ceria**: Lagu/tepuk anak pintar/praktik mandiri.
  * **🧠 Tantangan Nalar Kritis (Soal HOTS)**: Soal analisis studi kasus nyata moral dan akhlak.
  * **✏️ Ayo Berlatih**: Latihan formatif penguasaan konsep.

### 4. 📝 20 Soal Asesmen Sumatif Akhir Semester
* Memuat **20 Soal Pilihan Ganda** berkualitas tinggi mencakup seluruh materi semester.
* Dilengkapi lembar **Kunci Jawaban Lengkap (1–20)** di halaman terpisah.

### 5. 📋 Lembar Rubrik Penilaian Otentik Guru Resmi
* Dilengkapi instrumen penilaian resmi Kurikulum Merdeka yang sangat dibutuhkan guru sekolah:
  * **Tabel Rubrik Sikap (Afektif & Profil Pelajar Pancasila)** (Skor 1–4).
  * **Tabel Rubrik Pengetahuan & Keterampilan** (Skor 1–4).
  * Kolom Catatan & Umpan Balik Guru.
  * **Kolom Tanda Tangan Resmi**: Tanda tangan Orang Tua/Wali dan Guru Pengampu.

### 6. 🖼️ Smart Image Matcher & In-Browser Image Switcher
* **Pencocokan Otomatis Tanpa Kuota Limit**: Sistem cerdas mencocokkan kata kunci bab dengan perpustakaan ilustrasi 3D lokal beresolusi tinggi (bebas galat kuota API eksternal).
* **Anti-Duplikasi**: Setiap bab dijamin memiliki gambar yang bervariasi dan tidak kembar dengan cover.
* **Quick Switcher Dropdown**: Tersedia menu dropdown `🖼️ Ganti Gambar` di pojok gambar pada live preview untuk mengganti ilustrasi bab secara instan.
* **✏️ Edit Teks Langsung (`contenteditable`)**: Cukup aktifkan mode edit, lalu klik teks apa saja di modul untuk mengetik atau menyunting materi sebelum dicetak.

---

## 🛠️ Arsitektur & Teknologi

* **Backend**: Node.js, Express.js
* **AI Provider**: Google Gemini API (`gemini-flash-lite-latest`, `gemini-3.7-flash`, dll.) dengan sistem *auto-retry*, *exponential backoff*, dan *dynamic model discovery*.
* **Document Parsing**: `mammoth` (Word .docx), `pdf-parse` (PDF), `multer` (File upload)
* **Frontend UI**: HTML5, TailwindCSS, Interaktif iframe preview
* **Print Engine**: CSS Paged Media `@page { size: A4 portrait; margin: 0; }`

---

## 🚀 Panduan Instalasi & Menjalankan

### 1. Kloning Repositori
```bash
git clone https://github.com/dikkayulianto/ebook-generator.git
cd ebook-generator
```

### 2. Instal Dependensi
```bash
npm install
```

### 3. Jalankan Aplikasi
```bash
node server.js
```
Aplikasi akan aktif di: **[http://localhost:3000](http://localhost:3000)**

---

## 💡 Cara Penggunaan

1. Buka browser dan akses `http://localhost:3000`.
2. Masukkan **Gemini API Key** Anda (kunci disimpan aman di `localStorage` browser Anda).
3. Pilih **Tingkat Kelas SD (1–6)** dan **Semester**.
4. *(Opsional)* Unggah dokumen silabus atau buku acuan jika ingin struktur bab mengikuti file Anda.
5. Klik tombol **"✨ Generate E-Book Otomatis"**.
6. Gunakan fitur **"✏️ Edit Teks Langsung"** atau menu **"🖼️ Ganti Gambar"** jika ingin melakukan penyesuaian manual.
7. Klik tombol **"🖨️ Cetak / Download PDF"** (`Ctrl + P` $\rightarrow$ Simpan sebagai PDF) untuk mengekspor e-book berkualitas siap cetak!

---

## 📁 Struktur Direktori

```text
ebook-generator/
├── assets/                  # Koleksi ilustrasi 3D Pixar lokal (Cover & Bab)
├── exports/                 # Riwayat ekspor HTML modul ajar
├── public/                  # Dashboard antarmuka web (index.html)
├── uploads/                 # Direktori sementara unggahan file dokumen
├── server.js                # Server Express, routing API, & prompt AI engine
├── package.json             # Konfigurasi dependensi Node.js
└── README.md                # Dokumentasi proyek
```

---

## 📄 Lisensi

Didistribusikan di bawah lisensi MIT. Silakan gunakan, kembangkan, dan sesuaikan untuk kebutuhan edukasi serta komersial digital Anda.

## InScrape Pro - Instagram OSINT Automation Tool

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Instaloader-orange.svg" alt="Framework">
  <img src="https://img.shields.io/badge/Category-OSINT--Forensics-red.svg" alt="Category">
</p>

**InScrape Pro** adalah tool *Open Source Intelligence* (OSINT) berbasis CLI yang dirancang khusus untuk melakukan profiling, ekstraksi metadata, dan analisis relasi akun Instagram secara otomatis. Kode ini merupakan versi yang telah direfaktor penuh dengan penyesuaian API terbaru serta dilengkapi fitur *smart delay* untuk meminimalisir risiko pembatasan (*rate-limiting*) dari pihak Meta.

## ✨ Fitur Utama
*   **Comprehensive Profiling**: Menarik ID unik internal, biografi tautan, tipe akun (bisnis/personal), status verifikasi, hingga status privasi.
*   **Relationship Intelligence**: Melakukan dumping daftar pengikut (*followers*) dan yang diikuti (*following*) target.
*   **Anti-Block Mechanism**: Menggunakan modul jeda dinamis acak (*human behavior simulation*) untuk menjaga keamanan kredensial akun Anda.
*   **Cross-Platform UI**: Didukung oleh pewarnaan terminal via `colorama` yang kompatibel di Windows, Linux, maupun macOS.

## 🛠️ Struktur Proyek
```text
instagram-osint/
├── config/
│   └── __init__.py
├── src/
│   ├── __init__.py
│   ├── banner.py     # Manajemen aset visual & status log
│   ├── core.py       # Logika inti interaksi API Instagram
│   └── utils.py      # Pengaturan delay keamanan & validasi input
├── main.py           # Berkas eksekusi utama program
├── requirements.txt  # Daftar dependensi modul Python
└── README.md         # Dokumentasi repositori

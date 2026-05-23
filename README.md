## InScrape Instagram OSINT


Berbasis CLI yang dirancang khusus untuk melakukan profiling, ekstraksi metadata, dan analisis relasi akun Instagram secara otomatis. Kode ini merupakan versi yang telah direfaktor penuh dengan penyesuaian API terbaru serta dilengkapi fitur *smart delay* untuk meminimalisir risiko pembatasan (*rate-limiting*) dari pihak Meta.

## Fitur
*   **Comprehensive Profiling**: Menarik ID unik internal, biografi tautan, tipe akun (bisnis/personal), status verifikasi, hingga status privasi.
*   **Relationship Intelligence**: Melakukan dumping daftar pengikut (*followers*) dan yang diikuti (*following*) target.
*   **Anti-Block Mechanism**: Menggunakan modul jeda dinamis acak (*human behavior simulation*) untuk menjaga keamanan kredensial akun Anda.
*   **Cross-Platform UI**: Didukung oleh pewarnaan terminal via `colorama` yang kompatibel di Windows, Linux, maupun macOS.

## Instalasi & Penggunaan
​Clone Repositori :
```
git clone https://github.com/123tool/Instagram-Scraper-Osint.git
cd Instagram-Scraper-Osint
```
## Instalasi Dependensi
Pastikan Anda telah memasang Python 3.8 ke atas, kemudian eksekusi :
```
pip install -r requirements.txt
```
## Jalankan
```
python main.py
```

## Disclaimer

​Tool ini dibuat murni untuk tujuan edukasi, riset keamanan siber, dan analisis data terbuka (Open Source Intelligence). Gunakan akun tumbal (burner account) saat menjalankan automasi ini. Pengembang tidak bertanggung jawab atas segala bentuk pembatasan akun (checkpoint/banned) yang diakibatkan oleh penyalahgunaan batas wajar query rate pihak ketiga.

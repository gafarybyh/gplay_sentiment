# Analisis Sentimen Ulasan Aplikasi

=====================================

Proyek ini memungkinkan Anda untuk menganalisis sentimen ulasan aplikasi di google play menggunakan model machine learning. Proyek ini dapat membantu Anda memahami sentimen pengguna terhadap aplikasi Anda dan memberikan rekomendasi untuk perbaikan.

## Fitur Utama

---

-   **Scraping**: Otomatis ambil komentar dari app di Google Play Store
-   **Sentiment Analysis**: Menggunakan model multilingual / multibahasa (`modernBERT`) dari Hugging Face untuk menganalisis sentimen komentar
-   **Ringkasan Statistik**: Per aplikasi (jumlah ulasan, rata-rata skor, dsb)
-   **Laporan Otomatis**: Hasil analisis dijelaskan dan dibuat laporan menggunakan LLM (GEMINI)
-   **Hasil CSV & TXT**: Semua hasil analisis dan laporan disimpan di file

## Cara Menjalankan

---

### 1. Clone Repo

```bash
git clone [https://github.com/gafarybyh/gplay_sentiment.git](https://github.com/gafarybyh/gplay_sentiment.git)
cd gplay_sentiment
```

### 2. Buat Virtual Environment (Opsional)

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4 Siapkan File Environment

```
Buat file bernama .env seperti di .env.example di direktori utama proyek, lalu isi dengan konfigurasi berikut:

GEMINI_API_KEY = YOUR_API_KEY_HERE
GEMINI_MODEL = gemini-2.0-flash
```

### 5. Jalankan Program

```bash
python main.py
```

## Struktur Project
```
gplay_sentiment/
├── app/
│ ├── analyzer.py       # Pipeline analisis utama
│ ├── review_scraper.py # Scraping ulasan dari Google Play
│ ├── model_loader.py   # Load model BERT dan tokenizer
│ ├── llm_report.py     # Membuat prompt dan memanggil LLM
│ └── gemini.py         # Fungsi pemanggilan API Gemini
│
├── main.py             # Entry point program
├── requirements.txt    # Daftar dependensi
├── .env                # File Environment (Secrets)
└── README.md           # Dokumentasi proyek
```

## 🧪 Library yang Digunakan

- Python 3.10+
- Transformers
- Sentiment Multilingual Model (`modernBERT`)
- PyTorch
- Google Play Scraper
- Gemini API (LLM)

## 📤 Output yang Dihasilkan

- hasil_modernbertbase_YYYYMMDD_HHMMSS.csv
➤ Dataset lengkap ulasan beserta prediksi sentimen.

- laporan_sentimen_YYYYMMDD_HHMMSS.txt
➤ Laporan analisis sentimen otomatis dalam Bahasa Indonesia.

## 📝 Isi Laporan

Laporan yang dihasilkan oleh LLM mencakup:

-   Statistik ringkas per aplikasi
-   Analisis komentar negatif → Masalah yang sering muncul
-   Analisis komentar positif → Fitur yang disukai pengguna
-   Perbandingan performa antar aplikasi
-   Rekomendasi konkret bagi pengembang

## Contoh Hasil Laporan
```
**Laporan Analisis Sentimen Aplikasi E-commerce (Periode: 2025-05-19)**

**1. Ringkasan Sentimen:**

*   **Shopee:** Sentimen positif dominan, dengan skor rata-rata tertinggi (4.29). Pengguna umumnya puas dengan variasi produk, harga terjangkau, dan penanganan komplain. Namun, masalah saldo dan gangguan aplikasi menjadi perhatian.
*   **Tokopedia:** Sentimen lebih beragam, skor rata-rata (2.70). Pengguna menghargai pengiriman cepat dan variasi produk. Masalah utama meliputi kesulitan verifikasi akun, kurangnya gratis ongkir, dan masalah ekspedisi.
*   **Lazada:** Sentimen positif cukup baik, dengan skor rata-rata (3.65). Kecepatan pengiriman dan manfaat aplikasi dihargai. Keluhan meliputi fitur chat bermasalah, kesulitan paylater, dan masalah tanggung jawab seller.

**2. Masalah dari Komentar Negatif:**

*   **Shopee:** Masalah saldo ShopeePay, gangguan aplikasi, biaya pengiriman mahal, dan keluhan terhadap layanan kurir.
*   **Tokopedia:** Kesulitan verifikasi akun, kurangnya gratis ongkir, masalah ekspedisi, pelayanan pelanggan yang lambat, dan masalah promo.
*   **Lazada:** Fitur chat bermasalah, kesulitan paylater, kurangnya tanggung jawab seller, sering terjadi *bug* dan pembatalan pesanan, tidak bisa COD, dan pengiriman lambat.

**3. Fitur/Layanan Disukai Pengguna:**

*   **Shopee:** Variasi produk, harga terjangkau, penanganan komplain yang baik.
*   **Tokopedia:** Pengiriman cepat, variasi produk.
*   **Lazada:** Manfaat aplikasi untuk belanja kebutuhan sehari-hari.

**4. Perbandingan Performa Aplikasi:**

*   Shopee memiliki sentimen paling positif dan berhasil memuaskan pengguna dengan harga dan layanan.
*   Tokopedia perlu memperbaiki layanan pelanggan dan mengatasi masalah verifikasi akun.
*   Lazada perlu meningkatkan tanggung jawab seller dan memperbaiki masalah *bug* pada aplikasi.

**5. Saran untuk Pengembang:**

*   **Shopee:** Perbaiki masalah saldo ShopeePay dan optimalkan kinerja aplikasi agar tidak terjadi gangguan.
*   **Tokopedia:** Tingkatkan kualitas layanan pelanggan, pertimbangkan pemberian gratis ongkir, dan bekerja sama dengan penyedia logistik untuk meningkatkan kinerja pengiriman.
*   **Lazada:** Perbaiki fitur chat, permudah proses pendaftaran PayLater, dan pastikan seller bertanggung jawab atas produk yang dijual. Pertimbangkan untuk memberikan gratis ongkir tanpa minimal pembelian.

```

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
cd sentiment-analyzer
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

- Transformers - Hugging Face

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

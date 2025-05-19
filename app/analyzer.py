import pandas as pd
import re
from datetime import datetime
from torch.nn.functional import softmax
import torch
from app.model_loader import load_model_and_tokenizer
from app.review_scraper import scrape_reviews
from app.llm_report import generate_sentiment_report

# LOAD MODEL DAN TOKENIZER
tokenizer, model = load_model_and_tokenizer()

# FUNGSI UNTUK MEMBERSIHKAN TEKS
def clean_text(text):
    # Menghapus URL, username, dan karakter khusus
    text = re.sub(r"http\S+|www\S+|@\w+", "", text)
    # Menghapus karakter khusus
    text = re.sub(r"[^\w\s]", "", text)
    # Menghapus spasi berlebih
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

# FUNGSI PREDIKSI SENTIMEN
# Menggunakan model dan tokenizer yang telah di-load di model_loader.py
def analisa_sentimen_komentar(text):
    try:
        # Model menggunakan CPU
        # Jika tersedia GPU, gunakan GPU agar proses lebih cepat
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            probs = softmax(outputs.logits, dim=1)
            label = torch.argmax(probs, dim=1).item()
        labels = ['Negatif', 'Netral', 'Positif']
    
        return labels[label]
    
    except Exception as e:
        print(f"[ERROR] Proses analisa komentar: {e}")
        return None

# FUNGSI PRINT SUMMIRIZE
def print_ringkasan_sentimen(df):
    for app in df['App_ID'].unique():
        print(f"\nAplikasi: {app}")
        print(df[df['App_ID'] == app]['Sentimen'].value_counts())

# FUNGSI UTAMA ANALISIS APP
def run_analysis(app_ids: list[str], max_komentar: int = 100):
    """
    Args:
        app_ids: Daftar ID aplikasi yang akan diulas
        max_komentar: Jumlah ulasan per aplikasi
    """
    
    all_data = []
    
    # Mengambil ulasan setiap app_id
    for app_id in app_ids:
        
        revs = scrape_reviews(app_id, count=max_komentar)
        
        print(f"[INFO] Proses analisa ulasan {app_id}...")
        for r in revs:
            # Memeriksa apakah komentar memiliki minimal 3 kata
            text = r.get('content', '')
            score = r.get('score', 0)
            if not text or len(text.split()) < 3:
                continue
            # Bersihkan komentar
            cleaned = clean_text(text)
            
            # Analisa sentimen tiap komentar dan skor
            # Output sentimen (Negatif, Netral, Positif)
            sentiment = analisa_sentimen_komentar(f"{cleaned} (score: {score})")
            
            all_data.append({
                'App_ID': app_id,
                'Komentar': text,
                'Komentar_Bersih': cleaned,
                'Sentimen': sentiment,
                'Skor': r.get('score'),
                'Tanggal': r.get('at')
            })

    df = pd.DataFrame(all_data)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f"Analisis_{timestamp}.csv"
    
    # Simpan analisis ke CSV
    df.to_csv(f"{file_path}", index=False)
    
    print(f"[✓] Data analisa komentar telah disimpan di: {file_path}")

    if not df.empty:
        print_ringkasan_sentimen(df)
        report = generate_sentiment_report(df)

        print("\n[LAPORAN]:")
        print(report)

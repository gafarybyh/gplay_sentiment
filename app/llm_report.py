import pandas as pd
from datetime import datetime
from gemini.gemini import get_gemini_response

# FUNGSI UNTUK MENGAMBIL KOMENTAR PER APP
def ambil_komentar_app(df_app, max_comment_per_app=10):
    """
    Ambil komentar perkategori
    Args:
        df_app: DataFrame
        max_comment_perkategori: Jumlah maksimal komentar per app untuk prompt LLM
    
    """
    # Ambil komentar dan like
    pos = df_app[df_app['Sentimen'] == 'Positif'][['Komentar', 'Skor']].head(max_comment_per_app).values.tolist()
    neg = df_app[df_app['Sentimen'] == 'Negatif'][['Komentar', 'Skor']].head(max_comment_per_app).values.tolist()
    neu = df_app[df_app['Sentimen'] == 'Netral'][['Komentar', 'Skor']].head(max_comment_per_app).values.tolist()
    return pos, neg, neu

# FUNGSI UNTUK MEMBUAT LAPORAN MENGGUNAKAN GEMINI
def generate_sentiment_report(df):
    """
    Generate prompt untuk LLM dan buat laporan

    """
    summary = {
        'App_ID': [],
        'Total_Ulasan': [],
        'Positif': [],
        'Negatif': [],
        'Netral': [],
        'Rata_Rata_Skor': []
    }

    komentar_per_app = {}

    for app_id in df['App_ID'].unique():
        app_data = df[df['App_ID'] == app_id].copy()
        summary['App_ID'].append(app_id)
        summary['Total_Ulasan'].append(len(app_data))
        summary['Positif'].append((app_data['Sentimen'] == 'Positif').sum())
        summary['Negatif'].append((app_data['Sentimen'] == 'Negatif').sum())
        summary['Netral'].append((app_data['Sentimen'] == 'Netral').sum())
        skor = app_data['Skor'].dropna().mean()
        summary['Rata_Rata_Skor'].append(round(skor, 2) if not pd.isna(skor) else 0.0)
        
        pos, neg, neu = ambil_komentar_app(app_data)
        komentar_per_app[app_id] = {'positif': pos, 'negatif': neg, 'netral': neu}

    summary_df = pd.DataFrame(summary)

    prompt = f"Anda adalah seorang analis UX dan data.\n\n"
    prompt = f"Tanggal hari ini: {datetime.now().strftime('%Y-%m-%d')}.\n\n"
    prompt += "Statistik ulasan:\n\n"
    prompt += summary_df.to_string(index=False)
    prompt += "\nKomentar:\n"

    # Ambil komentar dan rating tiap app
    for app_id, komentar in komentar_per_app.items():
        prompt += f"\n== Aplikasi: {app_id} ==\n"
        prompt += "\n🟢 Komentar Positif:\n" + "\n".join(f"{i+1}. {k[0]} (Skor: {k[1]})" for i, k in enumerate(komentar['positif']))
        prompt += "\n\n🔴 Komentar Negatif:\n" + "\n".join(f"{i+1}. {k[0]} (Skor: {k[1]})" for i, k in enumerate(komentar['negatif']))
        prompt += "\n\n⚪ Komentar Netral:\n" + "\n".join(f"{i+1}. {k[0]} (Skor: {k[1]})" for i, k in enumerate(komentar['netral']))
        
        
    prompt += """
    
Tugas dan output Anda:
1. Ringkasan sentimen tiap aplikasi.
2. Masalah dari komentar negatif.
3. Fitur/layanan disukai pengguna.
4. Perbandingan Performa Aplikasi.
5. Saran untuk pengembang.

Tulis laporan dalam bahasa Indonesia yang jelas dan profesional, maksimal 400 kata. Pastikan laporan Anda memiliki struktur yang konsisten seperti output di atas tanpa tambahan kata.

"""

    try:
        print("[INFO] Proses membuat laporan...")
        
        # Buat laporan menggunakan GEMINI
        # print(f"[PROMPT GEMINI]: {prompt}")
        report = get_gemini_response(prompt)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = f"Analisis_Report_{timestamp}.txt"
        
        # Simpan laporan
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"[INFO] Laporan berhasil disimpan di: {file_path}")
        return report
        
    except Exception as e:
        report = f"[ERROR] Kesalahan membuat laporan GEMINI: {e}"

    

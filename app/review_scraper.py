from google_play_scraper import reviews, Sort

def scrape_reviews(app_id, lang='id', country='id', count=100):
    try:
        
        print(f"[INFO] Mengambil ulasan {app_id}...")
        
        # Mengambil ulasan dengan Sorting yang terbaru
        reviews_list, _ = reviews(app_id, lang=lang, country=country, count=count, sort=Sort.NEWEST)
        
        data_review = [
            {
                'userName': r.get('userName', ''),
                'content': r.get('content', ''),
                'thumbsUpCount': r.get('thumbsUpCount', 0),
                'score': r.get('score', None),
                'at': r.get('at', None)
            } for r in reviews_list
        ]
        
        if data_review:
            print(f"[INFO] Selesai mengambil ulasan {app_id}")
            return data_review
        
    except Exception as e:
        print(f"[ERROR] mengambil ulasan: {e}")
        return []

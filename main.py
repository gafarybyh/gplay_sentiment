from app.analyzer import run_analysis
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    app_ids = ['com.shopee.id', 'com.tokopedia.tkpd', 'com.lazada.android']
    
    run_analysis(
        app_ids=app_ids,
        max_komentar=100
    )

if __name__ == "__main__":
    main()
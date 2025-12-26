import requests
from bs4 import BeautifulSoup
import json

# Madam Coco analizi
print("=== MADAM COCO ANALİZİ ===")
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # Ana sayfa kontrol
    response = requests.get('https://www.madamcoco.com.tr', headers=headers, timeout=10)
    print(f"Madam Coco Status: {response.status_code}")
    
    # Kategori sayfası test
    response2 = requests.get('https://www.madamcoco.com.tr/ev-tekstili', headers=headers, timeout=10)
    print(f"Kategori sayfası Status: {response2.status_code}")
    
except Exception as e:
    print(f"Madam Coco Error: {e}")

print("\n=== ENGLISH HOME ANALİZİ ===")
try:
    response = requests.get('https://www.englishhome.com', headers=headers, timeout=10)
    print(f"English Home Status: {response.status_code}")
    
    # Kategori test
    response2 = requests.get('https://www.englishhome.com/ev-tekstili', headers=headers, timeout=10)
    print(f"Kategori sayfası Status: {response2.status_code}")
    
except Exception as e:
    print(f"English Home Error: {e}")


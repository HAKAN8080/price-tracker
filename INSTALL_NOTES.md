# 📁 Proje Yapısı

```
price_tracker/
│
├── 📱 Ana Uygulamalar
│   ├── price_tracker_app.py          # Streamlit Dashboard (ANA UYGULAMA)
│   ├── madamcoco_scraper.py          # Basic Web Scraper
│   └── selenium_scraper.py           # Gelişmiş Selenium Scraper
│
├── 🧪 Test & Yardımcı
│   ├── test_system.py                # Test ve örnek veri üretici
│   └── price_tracker_analysis.py    # Analiz fonksiyonları
│
├── 📊 Örnek Veriler
│   ├── sample_madamcoco.xlsx         # Madam Coco örnek Excel
│   ├── sample_madamcoco.csv          # Madam Coco örnek CSV
│   ├── sample_englishhome.xlsx       # English Home örnek Excel
│   ├── sample_englishhome.csv        # English Home örnek CSV
│   └── sample_comparison.csv         # Karşılaştırma örneği
│
├── 🚀 Başlatma Scriptleri
│   ├── start.sh                      # Linux/Mac başlatıcı
│   └── start.bat                     # Windows başlatıcı
│
└── 📚 Dokümantasyon
    ├── README.md                     # Ana dokümantasyon
    ├── requirements.txt              # Gerekli Python paketleri
    └── INSTALL_NOTES.md              # Bu dosya
```

---

## 🚀 Hızlı Başlangıç

### Windows Kullanıcıları:
```cmd
start.bat
```

### Linux/Mac Kullanıcıları:
```bash
./start.sh
```

### Manuel Başlatma:
```bash
# 1. Paketleri yükle
pip install -r requirements.txt

# 2. Dashboard'u başlat
streamlit run price_tracker_app.py
```

---

## 📋 Sistem Gereksinimleri

### Minimum:
- Python 3.8+
- 4GB RAM
- İnternet bağlantısı

### Önerilen:
- Python 3.10+
- 8GB RAM
- Chrome/Chromium tarayıcı (Selenium için)

### Gerekli Paketler:
```
streamlit >= 1.31.0
pandas >= 2.1.4
plotly >= 5.18.0
requests >= 2.31.0
beautifulsoup4 >= 4.12.3
selenium >= 4.16.0
openpyxl >= 3.1.2
```

---

## 🔧 Kurulum Adımları

### 1️⃣ Python Kurulumu
Windows: https://www.python.org/downloads/
Linux: `sudo apt install python3 python3-pip`
Mac: `brew install python3`

### 2️⃣ Proje Kurulumu
```bash
# Klasöre git
cd price_tracker

# Sanal ortam oluştur (opsiyonel ama önerilen)
python -m venv venv

# Sanal ortamı aktifleştir
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Paketleri yükle
pip install -r requirements.txt
```

### 3️⃣ Chrome WebDriver (Selenium için - opsiyonel)
1. Chrome tarayıcı yükle
2. ChromeDriver indir: https://chromedriver.chromium.org/
3. PATH'e ekle veya script ile aynı klasöre koy

---

## 🎯 Kullanım Senaryoları

### Senaryo 1: Hızlı Test
```bash
python test_system.py
```
- Örnek veriler oluşturur
- Sistemi test eder
- Karşılaştırma yapar

### Senaryo 2: Dashboard ile Analiz
```bash
streamlit run price_tracker_app.py
```
1. Tarayıcıda otomatik açılır
2. Sol menüden "Manuel Yükleme" seç
3. Örnek Excel dosyalarını yükle
4. "Analiz" sekmesine geç

### Senaryo 3: Otomatik Veri Çekme
```python
from selenium_scraper import SeleniumPriceScraper

scraper = SeleniumPriceScraper()
df = scraper.scrape_madamcoco_category(
    "https://www.madamcoco.com.tr/ev-tekstili",
    max_pages=5
)
df.to_csv('veriler.csv', encoding='utf-8-sig')
```

---

## 🐛 Sık Karşılaşılan Sorunlar

### Problem: "streamlit: command not found"
**Çözüm:**
```bash
pip install --upgrade streamlit
# veya
python -m streamlit run price_tracker_app.py
```

### Problem: Selenium ChromeDriver hatası
**Çözüm:**
```bash
# ChromeDriver otomatik yükleme
pip install webdriver-manager

# Script'te kullanım:
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```

### Problem: Türkçe karakter sorunu
**Çözüm:**
```python
# CSV okurken:
pd.read_csv('file.csv', encoding='utf-8-sig')

# CSV yazarken:
df.to_csv('file.csv', encoding='utf-8-sig', index=False)
```

### Problem: Port 8501 kullanımda
**Çözüm:**
```bash
streamlit run price_tracker_app.py --server.port 8502
```

---

## 📊 Veri Formatları

### Madam Coco Excel Formatı:
| Kolon | Tip | Açıklama |
|-------|-----|----------|
| source | str | "Madam Coco" |
| name | str | Ürün adı |
| sku | str | Ürün kodu |
| price | float | Güncel fiyat |
| old_price | float | Eski fiyat (opsiyonel) |
| discount_rate | float | İndirim oranı % |
| link | str | Ürün linki |
| image | str | Görsel URL |
| scraped_at | datetime | Çekilme tarihi |

### English Home Excel Formatı:
| Kolon | Tip | Açıklama |
|-------|-----|----------|
| source | str | "English Home" |
| name | str | Ürün adı |
| price | float | Güncel fiyat |
| link | str | Ürün linki |
| scraped_at | datetime | Çekilme tarihi |

---

## 🔒 Güvenlik ve Etik

### Web Scraping Kuralları:
✅ robots.txt dosyasına uyun
✅ Rate limiting kullanın (spam yapmayın)
✅ User-Agent belirtin
✅ Saygılı davranın

### Örnek robots.txt kontrolü:
```python
import requests

response = requests.get('https://www.madamcoco.com.tr/robots.txt')
print(response.text)
```

---

## 📈 Performans İpuçları

### 1. Çoklu Thread Kullanımı:
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(scrape_category, url) for url in urls]
```

### 2. Cache Kullanımı:
```python
import streamlit as st

@st.cache_data(ttl=3600)  # 1 saat cache
def load_data():
    return pd.read_csv('data.csv')
```

### 3. Batch Processing:
```python
# Büyük veri setlerini parçalara böl
chunks = [df[i:i+1000] for i in range(0, len(df), 1000)]
```

---

## 🔄 Güncellemeler

### Paket Güncellemeleri:
```bash
pip install --upgrade -r requirements.txt
```

### Sistem Kontrolü:
```bash
python test_system.py
```

---

## 📞 Destek

**Thorius Ltd**
- Web: www.siriusabcx.com
- Email: info@thorius.com
- Proje: AR4U Retail Analytics

---

## 📝 Lisans

Copyright © 2025 Thorius Ltd
Tüm hakları saklıdır.

---

## 🎉 Başarılı Kurulum Kontrolü

Sistem düzgün çalışıyorsa:
✅ `python test_system.py` hatasız çalışmalı
✅ `streamlit run price_tracker_app.py` dashboard açmalı
✅ Örnek Excel dosyaları yüklenmeli
✅ Karşılaştırma grafiği görünmeli

---

**Son Güncelleme:** 26 Aralık 2025
**Versiyon:** 1.0.0

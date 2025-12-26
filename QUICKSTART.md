# 🛍️ Madam Coco vs English Home - Fiyat Takip Sistemi

## ⚡ HIZLI BAŞLANGIÇ

### 1. İndir ve Aç
```bash
unzip price_tracker.zip
cd price_tracker
```

### 2. Çalıştır
**Windows:**
```cmd
start.bat
```

**Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

**veya Manuel:**
```bash
pip install -r requirements.txt
streamlit run price_tracker_app.py
```

### 3. Kullan
- Tarayıcıda http://localhost:8501 otomatik açılır
- Sol menüden "Manuel Yükleme" veya "Otomatik Çekme" seç
- Verileri yükle/çek
- "Analiz" sekmesine geç

---

## 📦 İÇİNDEKİLER

### Ana Dosyalar:
- `price_tracker_app.py` - **Streamlit Dashboard** (ANA UYGULAMA)
- `selenium_scraper.py` - Güçlü web scraper
- `madamcoco_scraper.py` - Basic scraper
- `test_system.py` - Test ve örnek veri

### Başlatıcılar:
- `start.bat` - Windows hızlı başlatıcı
- `start.sh` - Linux/Mac hızlı başlatıcı

### Örnek Veriler:
- `sample_madamcoco.xlsx` - Madam Coco örnek
- `sample_englishhome.xlsx` - English Home örnek
- `sample_comparison.csv` - Karşılaştırma örneği

### Dokümantasyon:
- `README.md` - Detaylı kullanım kılavuzu
- `INSTALL_NOTES.md` - Kurulum notları
- `requirements.txt` - Gerekli paketler

---

## ✨ ÖZELLİKLER

✅ **Otomatik Veri Çekme**
- Web scraping (Selenium)
- Kategori bazlı tarama
- Toplu veri toplama

✅ **Fiyat Karşılaştırma**
- Benzer ürün eşleştirme
- Fiyat farkı analizi
- İndirim oranı karşılaştırması

✅ **Dashboard**
- İnteraktif grafikler
- Filtreleme ve arama
- Excel/CSV export
- KPI göstergeleri

✅ **Raporlama**
- Detaylı tablolar
- Trend grafikleri
- Rekabet analizi
- Fiyat dağılımı

---

## 🎯 KULLANIM ÖRNEKLERİ

### Örnek 1: Test Verileri ile Başla
```bash
python test_system.py
streamlit run price_tracker_app.py
# Dashboard'da "Manuel Yükleme" seç
# sample_madamcoco.xlsx ve sample_englishhome.xlsx yükle
```

### Örnek 2: Madam Coco Veri Çek
```python
from selenium_scraper import SeleniumPriceScraper

scraper = SeleniumPriceScraper()
df = scraper.scrape_madamcoco_category(
    "https://www.madamcoco.com.tr/ev-tekstili",
    max_pages=5
)
df.to_csv('madamcoco_data.csv', encoding='utf-8-sig')
```

### Örnek 3: Dashboard ile Manuel Analiz
1. `streamlit run price_tracker_app.py`
2. Sol menü → "Manuel Yükleme"
3. Excel dosyalarını sürükle-bırak
4. "Analiz" sekmesi → Grafikler ve raporlar

---

## 📊 DASHBOARD ÖZELLİKLERİ

### Tab 1: Karşılaştırma 🆚
- Yan yana fiyat karşılaştırma
- Fiyat farkı ve yüzde
- Hangi mağaza ucuz?
- Filtreler ve arama

### Tab 2: Madam Coco 🏷️
- Tüm ürün listesi
- Fiyat filtreleme
- Arama
- İstatistikler

### Tab 3: English Home 🏷️
- Tüm ürün listesi
- Fiyat filtreleme
- Arama
- İstatistikler

### Tab 4: Grafikler 📈
- Fiyat karşılaştırma grafiği
- Fiyat farkı dağılımı
- Avantaj pasta grafiği

### Tab 5: Export 📥
- Excel/CSV indirme
- Karşılaştırma raporu
- Tüm veriler

---

## 🔧 GEREKSİNİMLER

- Python 3.8+
- Chrome tarayıcı (Selenium için)
- İnternet bağlantısı

**Otomatik Kurulum:**
```bash
pip install -r requirements.txt
```

**Manuel Kurulum:**
```bash
pip install streamlit pandas plotly requests beautifulsoup4 selenium openpyxl
```

---

## 🐛 SORUN GİDERME

### "streamlit: command not found"
```bash
python -m streamlit run price_tracker_app.py
```

### Selenium ChromeDriver hatası
```bash
pip install webdriver-manager
```

### Port kullanımda
```bash
streamlit run price_tracker_app.py --server.port 8502
```

### Türkçe karakter sorunu
CSV dosyalarında encoding='utf-8-sig' kullanılıyor

---

## 📞 DESTEK

**Thorius Ltd**
- Web: www.siriusabcx.com
- Proje: AR4U Retail Analytics Platform

---

## 🚀 GELİŞTİRME PLANI

- [ ] Otomatik email bildirimleri
- [ ] WhatsApp entegrasyonu
- [ ] Daha fazla rakip ekleme (LC Waikiki, Koton vs)
- [ ] AI destekli ürün eşleştirme
- [ ] Tarihsel fiyat grafikleri
- [ ] Mobil uygulama

---

**Versiyon:** 1.0.0  
**Tarih:** 26 Aralık 2025  
**Thorius Ltd © 2025**

---

## 🎉 HEMEN BAŞLA!

```bash
# 1. Paketi aç
unzip price_tracker.zip
cd price_tracker

# 2. Başlat
./start.sh  # veya start.bat

# 3. Kullan
# Tarayıcı otomatik açılacak!
```

**İyi Analizler! 🎊**

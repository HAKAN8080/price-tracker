# 🛍️ Price Tracker - Madam Coco vs English Home

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31+-red.svg)
![License](https://img.shields.io/badge/license-Proprietary-yellow.svg)

Madam Coco ve English Home mağazaları için kapsamlı fiyat takip ve karşılaştırma sistemi. Web scraping, veri analizi ve görselleştirme özellikleri içerir.

## 📸 Ekran Görüntüleri

> Dashboard'da karşılaştırmalı fiyat analizi, grafikler ve raporlama özellikleri bulunur.

## ✨ Özellikler

- 🔄 **Otomatik Veri Çekme**: Selenium ile güçlü web scraping
- 📊 **Karşılaştırmalı Analiz**: Benzer ürün eşleştirme ve fiyat karşılaştırma
- 📈 **Görselleştirme**: İnteraktif grafikler ve dashboard (Plotly)
- 📥 **Export**: Excel/CSV formatında veri indirme
- 🎯 **Filtreleme**: Kategori, fiyat ve benzerlik bazlı filtreleme
- 📱 **Responsive UI**: Modern Streamlit arayüzü

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8 veya üzeri
- Chrome/Chromium tarayıcı (Selenium için)

### Kurulum

```bash
# Repoyu klonla
git clone https://github.com/KULLANICI_ADINIZ/price-tracker.git
cd price-tracker

# Virtual environment oluştur (önerilen)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### Çalıştırma

**Seçenek 1: Hızlı Başlatıcı (Windows)**
```cmd
start.bat
```

**Seçenek 2: Hızlı Başlatıcı (Linux/Mac)**
```bash
chmod +x start.sh
./start.sh
```

**Seçenek 3: Manuel**
```bash
streamlit run price_tracker_app.py
```

Dashboard otomatik olarak `http://localhost:8501` adresinde açılacaktır.

## 📖 Kullanım

### 1. Test Verileri ile Başlama

```bash
python test_system.py
```

Bu komut örnek veriler oluşturur ve sistemi test eder.

### 2. Dashboard Kullanımı

1. Dashboard'u başlat
2. Sol menüden mod seç:
   - **Otomatik Çekme**: URL ile veri çekme
   - **Manuel Yükleme**: Excel/CSV yükleme
   - **Analiz**: Raporlar ve grafikler
3. Verileri yükle/çek
4. Karşılaştırma ve analiz sekmelerini incele

### 3. Python ile Kullanım

```python
from selenium_scraper import SeleniumPriceScraper

# Scraper oluştur
scraper = SeleniumPriceScraper()

# Madam Coco'dan veri çek
df_mc = scraper.scrape_madamcoco_category(
    "https://www.madamcoco.com.tr/ev-tekstili",
    max_pages=5
)

# English Home'dan veri çek
df_eh = scraper.scrape_englishhome_category(
    "https://www.englishhome.com/ev-tekstili",
    max_pages=5
)

# Kaydet
df_mc.to_csv('madamcoco_data.csv', encoding='utf-8-sig')
df_eh.to_csv('englishhome_data.csv', encoding='utf-8-sig')

# Scraper'ı kapat
scraper.close()
```

## 📁 Proje Yapısı

```
price-tracker/
│
├── price_tracker_app.py          # Ana Streamlit Dashboard
├── selenium_scraper.py           # Selenium bazlı scraper
├── madamcoco_scraper.py          # Requests/BeautifulSoup scraper
├── test_system.py                # Test ve örnek veri üretici
│
├── requirements.txt              # Python bağımlılıkları
├── .gitignore                    # Git ignore kuralları
├── README.md                     # Bu dosya
├── INSTALL_NOTES.md              # Detaylı kurulum notları
├── QUICKSTART.md                 # Hızlı başlangıç rehberi
│
├── start.sh                      # Linux/Mac başlatıcı
├── start.bat                     # Windows başlatıcı
│
└── sample_*.xlsx/csv             # Örnek veri dosyaları
```

## 🔧 Konfigürasyon

### Scraping Ayarları

`selenium_scraper.py` dosyasında:

```python
# Headless mode (arka planda çalışma)
scraper = SeleniumPriceScraper(headless=True)

# Maksimum sayfa sayısı
max_pages = 5

# Bekleme süresi (rate limiting)
time.sleep(2)
```

### Dashboard Ayarları

`price_tracker_app.py` dosyasında:

```python
# Benzerlik eşiği
min_similarity = 0.6  # %60

# Port değiştirme
streamlit run price_tracker_app.py --server.port 8502
```

## 📊 Veri Formatı

### Madam Coco Ürün Yapısı

```python
{
    'source': 'Madam Coco',
    'name': 'Ürün Adı',
    'sku': 'MC12345',
    'price': 299.99,
    'old_price': 399.99,
    'discount_rate': 25.0,
    'link': 'https://...',
    'image': 'https://...',
    'scraped_at': '2025-12-26 10:00:00'
}
```

### Karşılaştırma Yapısı

```python
{
    'madam_coco_product': 'Ürün A',
    'madam_coco_price': 299.99,
    'english_home_product': 'Benzer Ürün',
    'english_home_price': 279.99,
    'price_difference': 20.0,
    'price_difference_pct': 7.14,
    'similarity_score': 85.5,
    'cheaper_at': 'English Home'
}
```

## 🛠️ Teknolojiler

- **Python 3.8+**: Programlama dili
- **Streamlit**: Web dashboard framework
- **Selenium**: Web scraping (JavaScript destekli)
- **BeautifulSoup4**: HTML parsing
- **Pandas**: Veri manipülasyonu
- **Plotly**: İnteraktif grafikler
- **Requests**: HTTP istekleri

## 🐛 Sorun Giderme

### ChromeDriver Hatası

```bash
pip install webdriver-manager
```

Veya manuel olarak ChromeDriver indir: https://chromedriver.chromium.org/

### Port Kullanımda

```bash
streamlit run price_tracker_app.py --server.port 8502
```

### Türkçe Karakter Sorunu

CSV dosyalarında `encoding='utf-8-sig'` kullanıldı.

### Paket Hatası

```bash
pip install --upgrade -r requirements.txt
```

## 🔒 Güvenlik ve Etik

- ✅ `robots.txt` dosyalarına uyulmalıdır
- ✅ Rate limiting kullanılmalıdır
- ✅ User-Agent belirtilmelidir
- ✅ Spam yapılmamalıdır

## 📈 Gelecek Özellikler

- [ ] Email bildirimleri
- [ ] WhatsApp entegrasyonu
- [ ] Daha fazla mağaza desteği
- [ ] AI destekli ürün eşleştirme
- [ ] Tarihsel fiyat grafikleri
- [ ] Mobil uygulama
- [ ] API endpoint'leri

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📄 Lisans

Copyright © 2025 Thorius Ltd. Tüm hakları saklıdır.

Bu proje Thorius Ltd'ye aittir ve ticari kullanım için yetkilendirme gereklidir.

## 👥 Yazarlar

**Thorius Ltd**
- Website: [www.siriusabcx.com](https://www.siriusabcx.com)
- Email: info@thorius.com

## 🙏 Teşekkürler

- Streamlit ekibine harika framework için
- Selenium ve BeautifulSoup topluluklarına

## 📞 İletişim

Sorularınız için:
- 📧 Email: info@thorius.com
- 🌐 Website: www.siriusabcx.com
- 💼 LinkedIn: [Thorius Ltd](https://linkedin.com/company/thorius)

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**

---

<div align="center">
Made with ❤️ by Thorius Ltd
</div>

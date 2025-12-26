# 📁 Price Tracker - Klasör Yapısı

```
price-tracker/
│
├── 📄 Ana Dosyalar
│   ├── README.md                          # Ana dokümantasyon (GitHub anasayfa)
│   ├── LICENSE                            # MIT License
│   ├── CHANGELOG.md                       # Versiyon geçmişi
│   ├── CONTRIBUTING.md                    # Katkıda bulunma rehberi
│   ├── QUICKSTART.md                      # Hızlı başlangıç
│   ├── INSTALL_NOTES.md                   # Detaylı kurulum notları
│   ├── requirements.txt                   # Python bağımlılıkları
│   └── .gitignore                         # Git ignore kuralları
│
├── 🐍 Python Dosyaları
│   ├── price_tracker_app.py               # 🎨 Ana Streamlit Dashboard
│   ├── selenium_scraper.py                # 🔍 Selenium Web Scraper (güçlü)
│   ├── madamcoco_scraper.py               # 🔍 BeautifulSoup Scraper (basit)
│   ├── test_system.py                     # 🧪 Test ve örnek veri üretici
│   └── price_tracker_analysis.py          # 📊 Analiz fonksiyonları
│
├── 🚀 Başlatıcı Scriptler
│   ├── start.sh                           # Linux/Mac başlatıcı
│   └── start.bat                          # Windows başlatıcı
│
├── 📊 Örnek Veriler
│   ├── sample_madamcoco.xlsx              # Madam Coco örnek Excel
│   ├── sample_madamcoco.csv               # Madam Coco örnek CSV
│   ├── sample_englishhome.xlsx            # English Home örnek Excel
│   ├── sample_englishhome.csv             # English Home örnek CSV
│   └── sample_comparison.csv              # Karşılaştırma örneği
│
├── 📸 screenshots/                        # Ekran görüntüleri
│   ├── README.md                          # Screenshot rehberi
│   ├── dashboard.png                      # (eklenecek)
│   ├── comparison.png                     # (eklenecek)
│   └── charts.png                         # (eklenecek)
│
├── 📁 data/                               # Scraping verileri (gitignore'da)
│   ├── README.md                          # Data klasörü rehberi
│   ├── raw/                               # Ham veriler
│   │   ├── madamcoco/
│   │   └── englishhome/
│   ├── processed/                         # İşlenmiş veriler
│   └── archives/                          # Arşiv
│
├── 📚 docs/                               # Dokümantasyon
│   ├── index.md                           # Doküman index
│   ├── user-guide.md                      # (opsiyonel)
│   ├── api-reference.md                   # (opsiyonel)
│   └── architecture.md                    # (opsiyonel)
│
└── 🔧 .github/                            # GitHub konfigürasyonu
    ├── workflows/
    │   └── ci.yml                         # GitHub Actions CI/CD
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md                  # Bug rapor şablonu
    │   └── feature_request.md             # Özellik istek şablonu
    └── PULL_REQUEST_TEMPLATE.md           # PR şablonu
```

---

## 📝 Dosya Açıklamaları

### Ana Python Dosyaları

**price_tracker_app.py**
- Streamlit dashboard
- İnteraktif UI
- Karşılaştırma tabloları
- Grafikler ve raporlar
- Excel/CSV export

**selenium_scraper.py**
- Selenium WebDriver kullanır
- JavaScript destekli sitelerde çalışır
- Daha güvenilir
- Headless mode desteği
- Madam Coco ve English Home scraping

**madamcoco_scraper.py**
- Requests + BeautifulSoup
- Hızlı ve basit
- JavaScript olmayan siteler için
- Fiyat parse fonksiyonları
- Karşılaştırma algoritması

**test_system.py**
- Örnek veri üretir
- Sistemi test eder
- Demo için hazır

### Başlatıcı Scriptler

**start.sh** (Linux/Mac)
```bash
#!/bin/bash
# Menü ile kolay başlatma
# Python kurulum kontrolü
# Streamlit başlatma
```

**start.bat** (Windows)
```batch
@echo off
REM Windows menü
REM Dashboard başlatma
REM Test çalıştırma
```

### GitHub Yapısı

**.github/workflows/ci.yml**
- Otomatik test
- Python 3.8-3.11 matrix
- Lint (flake8)
- Build artifact

**.github/ISSUE_TEMPLATE/**
- Bug report şablonu
- Feature request şablonu
- Standart format

---

## 🎯 Önemli Notlar

### .gitignore İçeriği
```gitignore
# Python
__pycache__/
*.pyc
venv/

# Data
data/raw/
data/processed/
*_scraped.csv

# Selenium
chromedriver
*.exe

# IDE
.vscode/
.idea/
```

### requirements.txt İçeriği
```txt
streamlit==1.31.0
pandas==2.1.4
plotly==5.18.0
requests==2.31.0
beautifulsoup4==4.12.3
selenium==4.16.0
openpyxl==3.1.2
lxml==5.1.0
```

---

## 📦 Toplam Dosya Sayısı

- **Python dosyaları**: 5
- **Dokümantasyon**: 8
- **GitHub templates**: 4
- **Örnek veri**: 5
- **Script**: 2
- **Config**: 3

**TOPLAM**: 27 dosya + klasörler

---

## 🚀 GitHub'a Yükleme

1. **README.md zaten hazır** ✅
2. **.gitignore hazır** ✅
3. **LICENSE hazır** ✅
4. **GitHub Actions hazır** ✅
5. **Issue templates hazır** ✅

Sadece yükleyin! 🎉

---

**Thorius Ltd © 2025**

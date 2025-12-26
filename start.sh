#!/bin/bash

echo "🛍️ Madam Coco & English Home Fiyat Takip Sistemi"
echo "=================================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}1. Kurulum Kontrolü${NC}"
echo "-------------------"

# Python kontrolü
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Python3 yüklü: $(python3 --version)"
else
    echo "✗ Python3 bulunamadı! Lütfen yükleyin."
    exit 1
fi

# Pip kontrolü
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Pip yüklü"
else
    echo "✗ Pip bulunamadı! Lütfen yükleyin."
    exit 1
fi

# Paket kurulumu
echo ""
echo -e "${BLUE}2. Gerekli Paketleri Yükle${NC}"
echo "-------------------------"
read -p "Paketleri yüklemek ister misiniz? (E/h): " install
if [[ $install =~ ^[Ee]$ ]]; then
    echo "Paketler yükleniyor..."
    pip3 install -r requirements.txt
    echo -e "${GREEN}✓${NC} Paketler yüklendi"
fi

# Menü
echo ""
echo -e "${BLUE}3. Başlatma Seçenekleri${NC}"
echo "----------------------"
echo "1) 🖥️  Dashboard Başlat (Streamlit)"
echo "2) 🧪 Test Sistemi Çalıştır"
echo "3) 🔍 Selenium Scraper (Madam Coco)"
echo "4) 📊 Selenium Scraper (English Home)"
echo "5) 📚 Yardım / Dokümantasyon"
echo "6) ❌ Çıkış"
echo ""

read -p "Seçiminiz (1-6): " choice

case $choice in
    1)
        echo ""
        echo -e "${YELLOW}🚀 Streamlit Dashboard başlatılıyor...${NC}"
        echo "Tarayıcınızda http://localhost:8501 açılacak"
        echo ""
        streamlit run price_tracker_app.py
        ;;
    2)
        echo ""
        echo -e "${YELLOW}🧪 Test sistemi çalışıyor...${NC}"
        python3 test_system.py
        ;;
    3)
        echo ""
        echo -e "${YELLOW}🔍 Madam Coco scraper başlatılıyor...${NC}"
        read -p "Kategori URL: " url
        python3 -c "
from selenium_scraper import SeleniumPriceScraper
scraper = SeleniumPriceScraper()
df = scraper.scrape_madamcoco_category('$url', max_pages=3)
if not df.empty:
    df.to_csv('madamcoco_scraped.csv', index=False, encoding='utf-8-sig')
    print('✅ Veriler madamcoco_scraped.csv dosyasına kaydedildi')
scraper.close()
"
        ;;
    4)
        echo ""
        echo -e "${YELLOW}🔍 English Home scraper başlatılıyor...${NC}"
        read -p "Kategori URL: " url
        python3 -c "
from selenium_scraper import SeleniumPriceScraper
scraper = SeleniumPriceScraper()
df = scraper.scrape_englishhome_category('$url', max_pages=3)
if not df.empty:
    df.to_csv('englishhome_scraped.csv', index=False, encoding='utf-8-sig')
    print('✅ Veriler englishhome_scraped.csv dosyasına kaydedildi')
scraper.close()
"
        ;;
    5)
        echo ""
        cat README.md
        ;;
    6)
        echo ""
        echo "Çıkış yapılıyor..."
        exit 0
        ;;
    *)
        echo ""
        echo "Geçersiz seçim!"
        exit 1
        ;;
esac

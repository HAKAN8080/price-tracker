@echo off
chcp 65001 >nul
color 0A

echo ========================================================
echo 🛍️ Madam Coco ^& English Home Fiyat Takip Sistemi
echo ========================================================
echo.

:menu
echo.
echo 📋 MENÜ
echo --------
echo 1. 🖥️  Dashboard Başlat (Streamlit)
echo 2. 🧪 Test Sistemi Çalıştır
echo 3. 📦 Gerekli Paketleri Yükle
echo 4. 📊 Örnek Verileri Göster
echo 5. 📚 Yardım
echo 6. ❌ Çıkış
echo.

set /p choice="Seçiminiz (1-6): "

if "%choice%"=="1" goto dashboard
if "%choice%"=="2" goto test
if "%choice%"=="3" goto install
if "%choice%"=="4" goto samples
if "%choice%"=="5" goto help
if "%choice%"=="6" goto exit
goto menu

:dashboard
echo.
echo 🚀 Dashboard başlatılıyor...
echo.
streamlit run price_tracker_app.py
goto menu

:test
echo.
echo 🧪 Test sistemi çalışıyor...
echo.
python test_system.py
pause
goto menu

:install
echo.
echo 📦 Paketler yükleniyor...
echo.
pip install -r requirements.txt
echo.
echo ✅ Kurulum tamamlandı!
pause
goto menu

:samples
echo.
echo 📊 Örnek veriler açılıyor...
echo.
start sample_madamcoco.xlsx
start sample_englishhome.xlsx
start sample_comparison.csv
goto menu

:help
echo.
echo 📚 YARDIM
echo ---------
echo.
echo KULLANIM:
echo 1. İlk çalıştırmada "3" seçerek paketleri yükleyin
echo 2. "1" ile dashboard'u başlatın
echo 3. Tarayıcıda http://localhost:8501 açılacak
echo.
echo DASHBOARD ÖZELLİKLERİ:
echo - Otomatik veri çekme (URL ile)
echo - Manuel Excel/CSV yükleme
echo - Fiyat karşılaştırma
echo - Grafikler ve raporlar
echo.
echo DOSYALAR:
echo - price_tracker_app.py: Ana dashboard
echo - madamcoco_scraper.py: Basic scraper
echo - selenium_scraper.py: Gelişmiş scraper
echo - test_system.py: Test ve örnek veri
echo.
pause
goto menu

:exit
echo.
echo 👋 Çıkış yapılıyor...
echo.
exit

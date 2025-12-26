# Katkıda Bulunma Rehberi

Öncelikle, Price Tracker projesine katkıda bulunmayı düşündüğünüz için teşekkür ederiz! 🎉

## 🤝 Nasıl Katkıda Bulunabilirim?

### Bug Bildirimi

Bug bulduysanız, lütfen bir issue açın ve şunları ekleyin:
- Bug'ın açık bir tanımı
- Reproduce etme adımları
- Beklenen davranış
- Gerçek davranış
- Ekran görüntüleri (varsa)
- Python versiyonu ve işletim sistemi

### Özellik Önerisi

Yeni özellik önermek için:
- Issue açın ve "feature request" etiketi ekleyin
- Özelliğin ne yapacağını açıklayın
- Neden yararlı olacağını anlatın
- Varsa örnek kullanım senaryoları ekleyin

### Pull Request Süreci

1. **Fork edin**: Projeyi kendi hesabınıza fork edin

2. **Branch oluşturun**: Anlamlı bir isimle branch oluşturun
   ```bash
   git checkout -b feature/amazing-feature
   # veya
   git checkout -b fix/bug-description
   ```

3. **Kodlayın**: Değişikliklerinizi yapın
   - PEP 8 stil kılavuzuna uyun
   - Docstring'ler ekleyin
   - Yorumları Türkçe yazın (kullanıcı dostu)

4. **Test edin**: Kodunuzun çalıştığından emin olun
   ```bash
   python test_system.py
   ```

5. **Commit edin**: Anlamlı commit mesajları yazın
   ```bash
   git commit -m "feat: Add email notification feature"
   # veya
   git commit -m "fix: Resolve Turkish character encoding issue"
   ```

6. **Push edin**:
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Pull Request açın**: GitHub'da PR açın ve şunları ekleyin:
   - Değişikliklerin açıklaması
   - İlgili issue numarası (#123)
   - Test sonuçları
   - Ekran görüntüleri (UI değişiklikleri için)

## 📝 Kod Standartları

### Python Stil Kılavuzu

- PEP 8'e uyun
- Maksimum satır uzunluğu: 127 karakter
- Fonksiyon ve değişken isimleri: `snake_case`
- Class isimleri: `PascalCase`
- Sabitler: `UPPER_CASE`

### Docstring Formatı

```python
def scrape_category(url: str, max_pages: int = 5) -> pd.DataFrame:
    """
    Kategoriden ürünleri çeker.
    
    Args:
        url: Kategori URL'i
        max_pages: Maksimum sayfa sayısı
    
    Returns:
        Ürün bilgilerini içeren DataFrame
    
    Example:
        >>> scraper = Scraper()
        >>> df = scraper.scrape_category('https://...', max_pages=3)
    """
    pass
```

### Commit Mesaj Formatı

```
type: Kısa açıklama

Detaylı açıklama (opsiyonel)

Fixes #123
```

**Type'lar:**
- `feat`: Yeni özellik
- `fix`: Bug düzeltmesi
- `docs`: Dokümantasyon
- `style`: Kod formatı
- `refactor`: Kod yeniden yapılandırma
- `test`: Test ekleme/düzeltme
- `chore`: Bakım işleri

## 🧪 Test Gereksinimleri

Yeni özellikler için:
- Test case'leri ekleyin
- Mevcut testlerin geçtiğinden emin olun
- `test_system.py` çalışmalı

```bash
python test_system.py
```

## 📚 Dokümantasyon

Kod değişiklikleri için:
- Docstring'leri güncelleyin
- README.md'yi güncelleyin (gerekirse)
- INSTALL_NOTES.md'yi güncelleyin (gerekirse)
- Örnekler ekleyin

## 🏗️ Proje Yapısı

```
price-tracker/
├── price_tracker_app.py      # Ana dashboard
├── selenium_scraper.py       # Selenium scraper
├── madamcoco_scraper.py      # Basic scraper
├── test_system.py            # Test sistemi
├── requirements.txt          # Bağımlılıklar
└── docs/                     # Dokümantasyon
```

## 🔄 Development Workflow

1. Issue seç veya oluştur
2. Branch oluştur
3. Kod yaz
4. Test et
5. Commit et
6. Push et
7. PR aç
8. Code review bekle
9. Değişiklik yap (gerekirse)
10. Merge!

## 🎯 Öncelikli Alanlar

Yardıma ihtiyacımız olan konular:

1. **Performans İyileştirmeleri**
   - Scraping hızı
   - Dashboard yükleme süreleri
   - Veri işleme optimizasyonu

2. **Yeni Özellikler**
   - Email bildirimleri
   - WhatsApp entegrasyonu
   - Daha fazla mağaza desteği
   - AI destekli ürün eşleştirme

3. **Dokümantasyon**
   - Video tutoriallar
   - Daha fazla örnek
   - Multi-language support

4. **Test Coverage**
   - Unit testler
   - Integration testler
   - UI testler

## 🐛 Bug Fix Süreci

1. Bug'ı reproduce edin
2. Issue'ya yorum ekleyin
3. Fix için branch oluşturun
4. Test ekleyin (regression için)
5. PR açın

## 💬 İletişim

Sorularınız için:
- GitHub Issues
- Email: info@thorius.com
- Discussions sekmesi

## 📜 Lisans

Katkılarınız MIT License altında lisanslanacaktır.

## 🙏 Teşekkürler!

Katkılarınız için minnettarız! Her katkı, projeyi daha iyi hale getirir.

---

**Happy Coding! 🚀**

Thorius Ltd © 2025

"""
Fiyat Takip Sistemi - Test ve Örnek Kullanım
"""

import pandas as pd
from datetime import datetime
import json

# Örnek Madam Coco verisi
sample_madamcoco = [
    {
        'source': 'Madam Coco',
        'name': 'Pamuklu Çift Kişilik Nevresim Takımı',
        'sku': 'MC2024001',
        'price': 599.99,
        'old_price': 799.99,
        'discount_rate': 25.0,
        'link': 'https://www.madamcoco.com.tr/product/1',
        'image': 'https://example.com/image1.jpg',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'Madam Coco',
        'name': 'Dekoratif Yastık Kılıfı 45x45',
        'sku': 'MC2024002',
        'price': 149.99,
        'old_price': 199.99,
        'discount_rate': 25.0,
        'link': 'https://www.madamcoco.com.tr/product/2',
        'image': 'https://example.com/image2.jpg',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'Madam Coco',
        'name': 'Kadife Koltuk Örtüsü 170x270',
        'sku': 'MC2024003',
        'price': 899.99,
        'old_price': None,
        'discount_rate': 0,
        'link': 'https://www.madamcoco.com.tr/product/3',
        'image': 'https://example.com/image3.jpg',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'Madam Coco',
        'name': 'Banyo Havlusu Seti 4 Parça',
        'sku': 'MC2024004',
        'price': 299.99,
        'old_price': 399.99,
        'discount_rate': 25.0,
        'link': 'https://www.madamcoco.com.tr/product/4',
        'image': 'https://example.com/image4.jpg',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'Madam Coco',
        'name': 'Mutfak Önlüğü ve Eldiven Seti',
        'sku': 'MC2024005',
        'price': 199.99,
        'old_price': 249.99,
        'discount_rate': 20.0,
        'link': 'https://www.madamcoco.com.tr/product/5',
        'image': 'https://example.com/image5.jpg',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
]

# Örnek English Home verisi
sample_englishhome = [
    {
        'source': 'English Home',
        'name': 'Pamuklu Çift Kişilik Nevresim Seti',
        'price': 549.99,
        'link': 'https://www.englishhome.com/product/1',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'English Home',
        'name': 'Dekoratif Yastık 45x45 cm',
        'price': 139.99,
        'link': 'https://www.englishhome.com/product/2',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'English Home',
        'name': 'Koltuk Örtüsü Kadife 180x260',
        'price': 799.99,
        'link': 'https://www.englishhome.com/product/3',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'English Home',
        'name': 'Havlu Takımı 4lü Banyo',
        'price': 279.99,
        'link': 'https://www.englishhome.com/product/4',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'source': 'English Home',
        'name': 'Mutfak Önlük Eldiven Seti',
        'price': 179.99,
        'link': 'https://www.englishhome.com/product/5',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
]

def create_sample_data():
    """Örnek veri dosyaları oluştur"""
    
    # Excel dosyaları oluştur
    mc_df = pd.DataFrame(sample_madamcoco)
    eh_df = pd.DataFrame(sample_englishhome)
    
    mc_df.to_excel('sample_madamcoco.xlsx', index=False, engine='openpyxl')
    eh_df.to_excel('sample_englishhome.xlsx', index=False, engine='openpyxl')
    
    mc_df.to_csv('sample_madamcoco.csv', index=False, encoding='utf-8-sig')
    eh_df.to_csv('sample_englishhome.csv', index=False, encoding='utf-8-sig')
    
    print("✅ Örnek veri dosyaları oluşturuldu:")
    print("  - sample_madamcoco.xlsx")
    print("  - sample_englishhome.xlsx")
    print("  - sample_madamcoco.csv")
    print("  - sample_englishhome.csv")
    
    return mc_df, eh_df

def test_comparison():
    """Karşılaştırma algoritmasını test et"""
    from madamcoco_scraper import PriceComparator
    
    mc_df = pd.DataFrame(sample_madamcoco)
    eh_df = pd.DataFrame(sample_englishhome)
    
    print("\n📊 Karşılaştırma testi başlıyor...")
    comparison = PriceComparator.compare_products(mc_df, eh_df)
    
    print(f"\n✅ {len(comparison)} eşleşme bulundu\n")
    print(comparison.to_string())
    
    comparison.to_csv('sample_comparison.csv', index=False, encoding='utf-8-sig')
    print("\n💾 sample_comparison.csv kaydedildi")
    
    return comparison

def test_scraper():
    """Scraper fonksiyonlarını test et"""
    from madamcoco_scraper import MadamCocoScraper
    
    print("\n🧪 Scraper testi başlıyor...")
    scraper = MadamCocoScraper()
    
    # Kategori testi
    print("\n1️⃣ Kategorileri çekiyor...")
    categories = scraper.get_categories()
    
    if categories:
        print(f"✅ {len(categories)} kategori bulundu")
        for i, cat in enumerate(categories[:5], 1):
            print(f"  {i}. {cat['name']} - {cat['url']}")
    else:
        print("⚠️ Kategori bulunamadı (normal - ağ kısıtlaması)")
    
    # Fiyat parse testi
    print("\n2️⃣ Fiyat parse testi...")
    test_prices = [
        "₺299,99",
        "299.99 TL",
        "1.299,99",
        "TL 599,00"
    ]
    
    for price_text in test_prices:
        parsed = scraper.parse_price(price_text)
        print(f"  '{price_text}' → {parsed}")
    
    # İndirim hesaplama testi
    print("\n3️⃣ İndirim hesaplama testi...")
    test_cases = [
        (799.99, 599.99),
        (199.99, 149.99),
        (100, 75)
    ]
    
    for original, sale in test_cases:
        discount = scraper.calculate_discount(original, sale)
        print(f"  ₺{original} → ₺{sale} = %{discount} indirim")

def create_test_report():
    """Test raporu oluştur"""
    
    print("\n" + "="*60)
    print("📋 FİYAT TAKİP SİSTEMİ - TEST RAPORU")
    print("="*60)
    
    # Veri oluşturma
    print("\n1️⃣ ÖRNEK VERİ OLUŞTURMA")
    print("-" * 60)
    mc_df, eh_df = create_sample_data()
    
    # Karşılaştırma testi
    print("\n2️⃣ KARŞILAŞTIRMA TESTİ")
    print("-" * 60)
    comparison = test_comparison()
    
    # Scraper testi
    print("\n3️⃣ SCRAPER FONKSİYON TESTİ")
    print("-" * 60)
    test_scraper()
    
    # Özet
    print("\n" + "="*60)
    print("📊 ÖZET İSTATİSTİKLER")
    print("="*60)
    print(f"Madam Coco Ürün Sayısı: {len(mc_df)}")
    print(f"English Home Ürün Sayısı: {len(eh_df)}")
    print(f"Eşleşen Ürün Sayısı: {len(comparison)}")
    print(f"\nOrtalama Madam Coco Fiyat: ₺{mc_df['price'].mean():.2f}")
    print(f"Ortalama English Home Fiyat: ₺{eh_df['price'].mean():.2f}")
    
    if len(comparison) > 0:
        avg_diff = comparison['price_difference_pct'].mean()
        cheaper_mc = len(comparison[comparison['cheaper_at'] == 'Madam Coco'])
        cheaper_eh = len(comparison[comparison['cheaper_at'] == 'English Home'])
        
        print(f"\nOrtalama Fiyat Farkı: %{avg_diff:.2f}")
        print(f"Madam Coco Daha Ucuz: {cheaper_mc}/{len(comparison)}")
        print(f"English Home Daha Ucuz: {cheaper_eh}/{len(comparison)}")
    
    print("\n" + "="*60)
    print("✅ TEST TAMAMLANDI!")
    print("="*60)
    print("\n📁 Oluşturulan Dosyalar:")
    print("  - sample_madamcoco.xlsx")
    print("  - sample_englishhome.xlsx")
    print("  - sample_comparison.csv")
    
    print("\n🚀 Dashboard'u başlatmak için:")
    print("  streamlit run price_tracker_app.py")
    
    print("\n📖 Detaylı kullanım için:")
    print("  README.md dosyasını inceleyin")

if __name__ == "__main__":
    create_test_report()

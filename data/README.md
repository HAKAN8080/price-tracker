# Data Directory

Bu klasör, scraping işlemlerinden elde edilen verilerin saklanması için kullanılır.

## Klasör Yapısı

```
data/
├── raw/              # Ham scraping verileri
│   ├── madamcoco/
│   └── englishhome/
├── processed/        # İşlenmiş veriler
└── archives/         # Eski/yedek veriler
```

## Kullanım

Scraper'lar otomatik olarak bu klasöre veri kaydeder:

```python
# Örnek
df.to_csv('data/raw/madamcoco/products_2025-12-26.csv')
```

## Not

Bu klasör `.gitignore` dosyasında listelenmiştir ve Git'e yüklenmez.
Hassas verilerin yanlışlıkla paylaşılmasını önler.

"""
Madam Coco & English Home Fiyat Çekme Sistemi
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime
import time
from urllib.parse import urljoin
import re

class MadamCocoScraper:
    def __init__(self):
        self.base_url = "https://www.madamcoco.com.tr"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_categories(self):
        """Kategorileri çek"""
        try:
            response = self.session.get(self.base_url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            categories = []
            # Kategori linklerini bul
            nav_links = soup.find_all('a', href=re.compile(r'/([\w-]+)$'))
            
            for link in nav_links:
                href = link.get('href')
                text = link.get_text(strip=True)
                if href and text and len(text) > 2:
                    categories.append({
                        'name': text,
                        'url': urljoin(self.base_url, href)
                    })
            
            return categories
            
        except Exception as e:
            print(f"Kategori çekme hatası: {e}")
            return []
    
    def get_products_from_category(self, category_url, max_pages=5):
        """Kategoriden ürünleri çek"""
        products = []
        
        try:
            for page in range(1, max_pages + 1):
                url = f"{category_url}?page={page}"
                response = self.session.get(url, timeout=15)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Ürün kartlarını bul (class isimleri site yapısına göre değişecek)
                product_cards = soup.find_all(['div', 'article'], class_=re.compile(r'product|item|card'))
                
                if not product_cards:
                    break
                
                for card in product_cards:
                    try:
                        product = self.parse_product_card(card)
                        if product:
                            products.append(product)
                    except Exception as e:
                        continue
                
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            print(f"Ürün çekme hatası: {e}")
        
        return products
    
    def parse_product_card(self, card):
        """Ürün kartından bilgileri çıkar"""
        try:
            # Ürün adı
            name_elem = card.find(['h2', 'h3', 'a'], class_=re.compile(r'title|name|product'))
            name = name_elem.get_text(strip=True) if name_elem else None
            
            # Fiyat
            price_elem = card.find(['span', 'div'], class_=re.compile(r'price|fiyat'))
            price_text = price_elem.get_text(strip=True) if price_elem else None
            price = self.parse_price(price_text)
            
            # İndirimli fiyat
            sale_price_elem = card.find(['span', 'div'], class_=re.compile(r'sale|discount|indirim'))
            sale_price = self.parse_price(sale_price_elem.get_text(strip=True)) if sale_price_elem else None
            
            # Ürün linki
            link_elem = card.find('a', href=True)
            link = urljoin(self.base_url, link_elem['href']) if link_elem else None
            
            # Ürün kodu
            sku = None
            sku_elem = card.find(text=re.compile(r'SKU|Kod|Code', re.I))
            if sku_elem:
                sku = re.search(r'[\w-]+', sku_elem).group(0)
            
            # Görsel
            img_elem = card.find('img')
            image = img_elem.get('src') or img_elem.get('data-src') if img_elem else None
            
            if name and price:
                return {
                    'source': 'Madam Coco',
                    'name': name,
                    'sku': sku,
                    'price': price,
                    'sale_price': sale_price,
                    'discount_rate': self.calculate_discount(price, sale_price),
                    'link': link,
                    'image': image,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
        except Exception as e:
            pass
        
        return None
    
    def parse_price(self, price_text):
        """Fiyat metnini sayıya çevir"""
        if not price_text:
            return None
        
        # Sadece rakamları ve virgül/noktayı al
        price_clean = re.sub(r'[^\d,.]', '', price_text)
        price_clean = price_clean.replace('.', '').replace(',', '.')
        
        try:
            return float(price_clean)
        except:
            return None
    
    def calculate_discount(self, original, sale):
        """İndirim oranını hesapla"""
        if original and sale and original > sale:
            return round(((original - sale) / original) * 100, 2)
        return 0


class EnglishHomeScraper:
    def __init__(self):
        self.base_url = "https://www.englishhome.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_products_from_category(self, category_url, max_pages=5):
        """English Home kategorisinden ürün çek"""
        products = []
        
        try:
            for page in range(1, max_pages + 1):
                url = f"{category_url}?page={page}"
                response = self.session.get(url, timeout=15)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                product_cards = soup.find_all(['div', 'article'], class_=re.compile(r'product|item|card'))
                
                if not product_cards:
                    break
                
                for card in product_cards:
                    try:
                        product = self.parse_product_card(card)
                        if product:
                            products.append(product)
                    except:
                        continue
                
                time.sleep(1)
                
        except Exception as e:
            print(f"English Home çekme hatası: {e}")
        
        return products
    
    def parse_product_card(self, card):
        """Ürün kartını parse et"""
        try:
            name_elem = card.find(['h2', 'h3', 'a'], class_=re.compile(r'title|name|product'))
            name = name_elem.get_text(strip=True) if name_elem else None
            
            price_elem = card.find(['span', 'div'], class_=re.compile(r'price|fiyat'))
            price_text = price_elem.get_text(strip=True) if price_elem else None
            price = self.parse_price(price_text)
            
            link_elem = card.find('a', href=True)
            link = urljoin(self.base_url, link_elem['href']) if link_elem else None
            
            if name and price:
                return {
                    'source': 'English Home',
                    'name': name,
                    'price': price,
                    'link': link,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
        except:
            pass
        
        return None
    
    def parse_price(self, price_text):
        """Fiyat parse"""
        if not price_text:
            return None
        
        price_clean = re.sub(r'[^\d,.]', '', price_text)
        price_clean = price_clean.replace('.', '').replace(',', '.')
        
        try:
            return float(price_clean)
        except:
            return None


class PriceComparator:
    """Fiyat karşılaştırma motoru"""
    
    @staticmethod
    def compare_products(madamcoco_df, englishhome_df):
        """İki mağaza arasında ürün karşılaştırması yap"""
        comparisons = []
        
        for _, mc_product in madamcoco_df.iterrows():
            # Benzer ürünleri bul (isim benzerliği)
            mc_name = mc_product['name'].lower()
            
            for _, eh_product in englishhome_df.iterrows():
                eh_name = eh_product['name'].lower()
                
                # Basit benzerlik kontrolü
                similarity = PriceComparator.calculate_similarity(mc_name, eh_name)
                
                if similarity > 0.6:  # %60 benzerlik eşiği
                    price_diff = mc_product['price'] - eh_product['price']
                    price_diff_pct = (price_diff / eh_product['price']) * 100
                    
                    comparisons.append({
                        'madam_coco_product': mc_product['name'],
                        'madam_coco_price': mc_product['price'],
                        'english_home_product': eh_product['name'],
                        'english_home_price': eh_product['price'],
                        'price_difference': price_diff,
                        'price_difference_pct': round(price_diff_pct, 2),
                        'similarity_score': round(similarity * 100, 2),
                        'cheaper_at': 'Madam Coco' if price_diff < 0 else 'English Home'
                    })
        
        return pd.DataFrame(comparisons)
    
    @staticmethod
    def calculate_similarity(str1, str2):
        """İki string arasındaki benzerliği hesapla"""
        # Basit kelime eşleştirme
        words1 = set(str1.split())
        words2 = set(str2.split())
        
        if not words1 or not words2:
            return 0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)


def main():
    """Ana çalıştırma fonksiyonu"""
    print("🛍️ Fiyat Takip Sistemi Başlatılıyor...")
    
    # Madam Coco scraper
    mc_scraper = MadamCocoScraper()
    print("\n📊 Madam Coco kategorileri alınıyor...")
    categories = mc_scraper.get_categories()
    
    if categories:
        print(f"✅ {len(categories)} kategori bulundu")
        for cat in categories[:5]:
            print(f"  - {cat['name']}")
    
    # English Home scraper
    eh_scraper = EnglishHomeScraper()
    
    print("\n✅ Sistem hazır!")
    print("\nKullanım:")
    print("1. mc_scraper.get_products_from_category(category_url)")
    print("2. eh_scraper.get_products_from_category(category_url)")
    print("3. PriceComparator.compare_products(df1, df2)")


if __name__ == "__main__":
    main()

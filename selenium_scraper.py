"""
Selenium ile Madam Coco & English Home Fiyat Scraper
Daha güçlü ve JavaScript destekli
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
from datetime import datetime
import time
import re

class SeleniumPriceScraper:
    def __init__(self, headless=True):
        """Selenium driver kurulumu"""
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument('--headless')
        
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def scrape_madamcoco_category(self, category_url, max_pages=5):
        """Madam Coco kategorisinden ürünleri çek"""
        all_products = []
        
        try:
            for page in range(1, max_pages + 1):
                url = f"{category_url}?page={page}"
                print(f"Sayfa {page} çekiliyor: {url}")
                
                self.driver.get(url)
                time.sleep(3)  # Sayfa yüklenmesini bekle
                
                # Scroll down to load lazy images
                self.scroll_page()
                
                # Ürün kartlarını bul
                products = self.extract_madamcoco_products()
                
                if not products:
                    print(f"Sayfa {page}'de ürün bulunamadı, durduruluyor")
                    break
                
                all_products.extend(products)
                print(f"✅ {len(products)} ürün çekildi")
                
                time.sleep(2)  # Rate limiting
            
            print(f"\n🎉 Toplam {len(all_products)} ürün çekildi!")
            return pd.DataFrame(all_products)
            
        except Exception as e:
            print(f"❌ Hata: {e}")
            return pd.DataFrame(all_products) if all_products else pd.DataFrame()
    
    def extract_madamcoco_products(self):
        """Sayfadaki Madam Coco ürünlerini çıkar"""
        products = []
        
        # Farklı olası selektorları dene
        selectors = [
            "div.product-item",
            "div.product-card",
            "article.product",
            "div[data-product]",
            ".product-list-item"
        ]
        
        product_elements = []
        for selector in selectors:
            try:
                product_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if product_elements:
                    break
            except:
                continue
        
        for element in product_elements:
            try:
                product = self.parse_madamcoco_product(element)
                if product:
                    products.append(product)
            except Exception as e:
                continue
        
        return products
    
    def parse_madamcoco_product(self, element):
        """Tek bir Madam Coco ürün elementini parse et"""
        try:
            # Ürün adı
            name_selectors = [
                ".product-name",
                ".product-title",
                "h3",
                "h2",
                "a.product-link"
            ]
            name = self.get_text_from_selectors(element, name_selectors)
            
            # Fiyat
            price_selectors = [
                ".product-price",
                ".price",
                "span.price-value",
                ".sale-price"
            ]
            price_text = self.get_text_from_selectors(element, price_selectors)
            price = self.parse_price(price_text)
            
            # Eski fiyat (indirim varsa)
            old_price_selectors = [
                ".old-price",
                ".original-price",
                "span.line-through"
            ]
            old_price_text = self.get_text_from_selectors(element, old_price_selectors)
            old_price = self.parse_price(old_price_text)
            
            # Link
            link = None
            try:
                link_elem = element.find_element(By.TAG_NAME, "a")
                link = link_elem.get_attribute("href")
            except:
                pass
            
            # Görsel
            image = None
            try:
                img_elem = element.find_element(By.TAG_NAME, "img")
                image = img_elem.get_attribute("src") or img_elem.get_attribute("data-src")
            except:
                pass
            
            # Ürün kodu
            sku = self.extract_sku(element)
            
            if name and price:
                return {
                    'source': 'Madam Coco',
                    'name': name,
                    'sku': sku,
                    'price': price,
                    'old_price': old_price,
                    'discount_rate': self.calculate_discount(old_price, price),
                    'link': link,
                    'image': image,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
        
        except Exception as e:
            pass
        
        return None
    
    def scrape_englishhome_category(self, category_url, max_pages=5):
        """English Home kategorisinden ürünleri çek"""
        all_products = []
        
        try:
            for page in range(1, max_pages + 1):
                url = f"{category_url}?page={page}"
                print(f"Sayfa {page} çekiliyor: {url}")
                
                self.driver.get(url)
                time.sleep(3)
                
                self.scroll_page()
                products = self.extract_englishhome_products()
                
                if not products:
                    print(f"Sayfa {page}'de ürün bulunamadı, durduruluyor")
                    break
                
                all_products.extend(products)
                print(f"✅ {len(products)} ürün çekildi")
                
                time.sleep(2)
            
            print(f"\n🎉 Toplam {len(all_products)} ürün çekildi!")
            return pd.DataFrame(all_products)
            
        except Exception as e:
            print(f"❌ Hata: {e}")
            return pd.DataFrame(all_products) if all_products else pd.DataFrame()
    
    def extract_englishhome_products(self):
        """English Home ürünlerini çıkar"""
        products = []
        
        selectors = [
            "div.product-item",
            "div.product-card",
            "article.product",
            "div[data-product]"
        ]
        
        product_elements = []
        for selector in selectors:
            try:
                product_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if product_elements:
                    break
            except:
                continue
        
        for element in product_elements:
            try:
                product = self.parse_englishhome_product(element)
                if product:
                    products.append(product)
            except:
                continue
        
        return products
    
    def parse_englishhome_product(self, element):
        """English Home ürün parse"""
        try:
            name = self.get_text_from_selectors(element, [".product-name", ".product-title", "h3", "h2"])
            price_text = self.get_text_from_selectors(element, [".product-price", ".price", "span.price-value"])
            price = self.parse_price(price_text)
            
            link = None
            try:
                link_elem = element.find_element(By.TAG_NAME, "a")
                link = link_elem.get_attribute("href")
            except:
                pass
            
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
    
    def get_text_from_selectors(self, element, selectors):
        """Birden fazla selector dene, ilk bulduğu metni döndür"""
        for selector in selectors:
            try:
                elem = element.find_element(By.CSS_SELECTOR, selector)
                text = elem.text.strip()
                if text:
                    return text
            except:
                continue
        return None
    
    def extract_sku(self, element):
        """Ürün kodunu çıkar"""
        try:
            text = element.text
            sku_match = re.search(r'SKU[:\s]+([A-Z0-9-]+)', text, re.I)
            if sku_match:
                return sku_match.group(1)
            
            # data-sku attribute kontrol
            sku = element.get_attribute('data-sku')
            if sku:
                return sku
        except:
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
    
    def calculate_discount(self, old_price, current_price):
        """İndirim oranını hesapla"""
        if old_price and current_price and old_price > current_price:
            return round(((old_price - current_price) / old_price) * 100, 2)
        return 0
    
    def scroll_page(self):
        """Sayfayı scroll et (lazy loading için)"""
        try:
            # Scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            # Scroll back to top
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(0.5)
        except:
            pass
    
    def close(self):
        """Driver'ı kapat"""
        try:
            self.driver.quit()
        except:
            pass
    
    def __del__(self):
        """Destructor - driver'ı otomatik kapat"""
        self.close()


# Kullanım örneği
if __name__ == "__main__":
    print("🚀 Selenium Scraper Başlatılıyor...\n")
    
    scraper = SeleniumPriceScraper(headless=True)
    
    # Madam Coco
    print("📊 Madam Coco Ev Tekstili Çekiliyor...")
    mc_df = scraper.scrape_madamcoco_category(
        "https://www.madamcoco.com.tr/ev-tekstili",
        max_pages=3
    )
    
    if not mc_df.empty:
        print(f"\n✅ {len(mc_df)} Madam Coco ürünü çekildi")
        mc_df.to_csv('madamcoco_products.csv', index=False, encoding='utf-8-sig')
        print("💾 madamcoco_products.csv kaydedildi")
    
    # English Home
    print("\n📊 English Home Ev Tekstili Çekiliyor...")
    eh_df = scraper.scrape_englishhome_category(
        "https://www.englishhome.com/ev-tekstili",
        max_pages=3
    )
    
    if not eh_df.empty:
        print(f"\n✅ {len(eh_df)} English Home ürünü çekildi")
        eh_df.to_csv('englishhome_products.csv', index=False, encoding='utf-8-sig')
        print("💾 englishhome_products.csv kaydedildi")
    
    scraper.close()
    print("\n🎉 Tamamlandı!")

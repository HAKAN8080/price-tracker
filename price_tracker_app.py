"""
Madam Coco & English Home Fiyat Takip Dashboard
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from madamcoco_scraper import MadamCocoScraper, EnglishHomeScraper, PriceComparator
import json
import time

st.set_page_config(
    page_title="Fiyat Takip Sistemi",
    page_icon="🛍️",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .price-positive {
        color: #10b981;
        font-weight: bold;
    }
    .price-negative {
        color: #ef4444;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Session state
if 'madamcoco_data' not in st.session_state:
    st.session_state.madamcoco_data = None
if 'englishhome_data' not in st.session_state:
    st.session_state.englishhome_data = None
if 'comparison_data' not in st.session_state:
    st.session_state.comparison_data = None
if 'scraping_history' not in st.session_state:
    st.session_state.scraping_history = []

st.title("🛍️ Madam Coco vs English Home - Fiyat Takip Sistemi")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Ayarlar")
    
    mode = st.radio(
        "Mod Seçin",
        ["🔄 Otomatik Çekme", "📤 Manuel Yükleme", "📊 Analiz"]
    )
    
    st.markdown("---")
    
    if mode == "🔄 Otomatik Çekme":
        st.subheader("Scraping Ayarları")
        
        scrape_source = st.selectbox(
            "Kaynak",
            ["Madam Coco", "English Home", "Her İkisi"]
        )
        
        category_url = st.text_input(
            "Kategori URL",
            placeholder="https://www.madamcoco.com.tr/ev-tekstili"
        )
        
        max_pages = st.slider("Maksimum Sayfa", 1, 10, 3)
        
        if st.button("🚀 Verileri Çek"):
            if category_url:
                with st.spinner("Veriler çekiliyor..."):
                    try:
                        if scrape_source == "Madam Coco" or scrape_source == "Her İkisi":
                            mc_scraper = MadamCocoScraper()
                            mc_products = mc_scraper.get_products_from_category(category_url, max_pages)
                            
                            if mc_products:
                                st.session_state.madamcoco_data = pd.DataFrame(mc_products)
                                st.success(f"✅ {len(mc_products)} Madam Coco ürünü çekildi!")
                                
                                # Geçmişe ekle
                                st.session_state.scraping_history.append({
                                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                    'source': 'Madam Coco',
                                    'count': len(mc_products),
                                    'url': category_url
                                })
                            else:
                                st.warning("⚠️ Madam Coco'dan ürün çekilemedi")
                        
                        if scrape_source == "English Home" or scrape_source == "Her İkisi":
                            eh_scraper = EnglishHomeScraper()
                            eh_products = eh_scraper.get_products_from_category(category_url, max_pages)
                            
                            if eh_products:
                                st.session_state.englishhome_data = pd.DataFrame(eh_products)
                                st.success(f"✅ {len(eh_products)} English Home ürünü çekildi!")
                                
                                st.session_state.scraping_history.append({
                                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                    'source': 'English Home',
                                    'count': len(eh_products),
                                    'url': category_url
                                })
                            else:
                                st.warning("⚠️ English Home'dan ürün çekilemedi")
                        
                        # Karşılaştırma yap
                        if st.session_state.madamcoco_data is not None and st.session_state.englishhome_data is not None:
                            st.session_state.comparison_data = PriceComparator.compare_products(
                                st.session_state.madamcoco_data,
                                st.session_state.englishhome_data
                            )
                            
                    except Exception as e:
                        st.error(f"❌ Hata: {e}")
            else:
                st.warning("⚠️ Lütfen kategori URL girin")
    
    elif mode == "📤 Manuel Yükleme":
        st.subheader("Excel/CSV Yükle")
        
        mc_file = st.file_uploader("Madam Coco Excel", type=['xlsx', 'csv'])
        if mc_file:
            if mc_file.name.endswith('.csv'):
                st.session_state.madamcoco_data = pd.read_csv(mc_file)
            else:
                st.session_state.madamcoco_data = pd.read_excel(mc_file)
            st.success(f"✅ {len(st.session_state.madamcoco_data)} ürün yüklendi")
        
        eh_file = st.file_uploader("English Home Excel", type=['xlsx', 'csv'])
        if eh_file:
            if eh_file.name.endswith('.csv'):
                st.session_state.englishhome_data = pd.read_csv(eh_file)
            else:
                st.session_state.englishhome_data = pd.read_excel(eh_file)
            st.success(f"✅ {len(st.session_state.englishhome_data)} ürün yüklendi")
    
    st.markdown("---")
    st.caption("Thorius Ltd © 2025")

# Ana içerik
if mode == "📊 Analiz" or st.session_state.comparison_data is not None:
    
    # KPI'lar
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mc_count = len(st.session_state.madamcoco_data) if st.session_state.madamcoco_data is not None else 0
        st.metric("Madam Coco Ürün", mc_count, delta=None)
    
    with col2:
        eh_count = len(st.session_state.englishhome_data) if st.session_state.englishhome_data is not None else 0
        st.metric("English Home Ürün", eh_count, delta=None)
    
    with col3:
        comp_count = len(st.session_state.comparison_data) if st.session_state.comparison_data is not None else 0
        st.metric("Karşılaştırılabilir Ürün", comp_count, delta=None)
    
    with col4:
        if st.session_state.comparison_data is not None and len(st.session_state.comparison_data) > 0:
            cheaper_count = len(st.session_state.comparison_data[st.session_state.comparison_data['cheaper_at'] == 'Madam Coco'])
            st.metric("Madam Coco Avantaj", f"{cheaper_count}/{comp_count}")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Karşılaştırma",
        "🏷️ Madam Coco",
        "🏷️ English Home",
        "📈 Grafikler",
        "📥 Export"
    ])
    
    with tab1:
        st.subheader("🆚 Fiyat Karşılaştırması")
        
        if st.session_state.comparison_data is not None and len(st.session_state.comparison_data) > 0:
            df_comp = st.session_state.comparison_data.copy()
            
            # Filtreler
            col1, col2 = st.columns(2)
            with col1:
                price_filter = st.selectbox(
                    "Fiyat Filtresi",
                    ["Tümü", "Madam Coco Ucuz", "English Home Ucuz"]
                )
            
            with col2:
                min_similarity = st.slider("Minimum Benzerlik (%)", 0, 100, 60)
            
            # Filtreleme
            if price_filter == "Madam Coco Ucuz":
                df_comp = df_comp[df_comp['cheaper_at'] == 'Madam Coco']
            elif price_filter == "English Home Ucuz":
                df_comp = df_comp[df_comp['cheaper_at'] == 'English Home']
            
            df_comp = df_comp[df_comp['similarity_score'] >= min_similarity]
            
            # Tablo
            st.dataframe(
                df_comp[[
                    'madam_coco_product', 'madam_coco_price',
                    'english_home_product', 'english_home_price',
                    'price_difference', 'price_difference_pct',
                    'cheaper_at', 'similarity_score'
                ]].style.background_gradient(subset=['price_difference_pct'], cmap='RdYlGn_r'),
                use_container_width=True,
                height=400
            )
            
            # Özet istatistikler
            st.markdown("### 📊 Özet İstatistikler")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                avg_mc = df_comp['madam_coco_price'].mean()
                st.metric("Ortalama Madam Coco Fiyat", f"₺{avg_mc:.2f}")
            
            with col2:
                avg_eh = df_comp['english_home_price'].mean()
                st.metric("Ortalama English Home Fiyat", f"₺{avg_eh:.2f}")
            
            with col3:
                avg_diff = df_comp['price_difference_pct'].mean()
                st.metric("Ortalama Fiyat Farkı", f"%{avg_diff:.2f}")
        
        else:
            st.info("ℹ️ Karşılaştırma için veri yükleyin veya çekin")
    
    with tab2:
        st.subheader("🏷️ Madam Coco Ürünleri")
        
        if st.session_state.madamcoco_data is not None:
            df_mc = st.session_state.madamcoco_data.copy()
            
            # Arama
            search = st.text_input("🔍 Ürün Ara", key="mc_search")
            if search:
                df_mc = df_mc[df_mc['name'].str.contains(search, case=False, na=False)]
            
            # Fiyat filtreleme
            col1, col2 = st.columns(2)
            with col1:
                min_price = st.number_input("Min Fiyat", 0.0, value=0.0, key="mc_min")
            with col2:
                max_price = st.number_input("Max Fiyat", 0.0, value=10000.0, key="mc_max")
            
            df_mc = df_mc[(df_mc['price'] >= min_price) & (df_mc['price'] <= max_price)]
            
            st.dataframe(df_mc, use_container_width=True, height=400)
            
            # İstatistikler
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Toplam Ürün", len(df_mc))
            with col2:
                st.metric("Ortalama Fiyat", f"₺{df_mc['price'].mean():.2f}")
            with col3:
                st.metric("En Düşük", f"₺{df_mc['price'].min():.2f}")
            with col4:
                st.metric("En Yüksek", f"₺{df_mc['price'].max():.2f}")
        else:
            st.info("ℹ️ Madam Coco verisi yok")
    
    with tab3:
        st.subheader("🏷️ English Home Ürünleri")
        
        if st.session_state.englishhome_data is not None:
            df_eh = st.session_state.englishhome_data.copy()
            
            search = st.text_input("🔍 Ürün Ara", key="eh_search")
            if search:
                df_eh = df_eh[df_eh['name'].str.contains(search, case=False, na=False)]
            
            col1, col2 = st.columns(2)
            with col1:
                min_price = st.number_input("Min Fiyat", 0.0, value=0.0, key="eh_min")
            with col2:
                max_price = st.number_input("Max Fiyat", 0.0, value=10000.0, key="eh_max")
            
            df_eh = df_eh[(df_eh['price'] >= min_price) & (df_eh['price'] <= max_price)]
            
            st.dataframe(df_eh, use_container_width=True, height=400)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Toplam Ürün", len(df_eh))
            with col2:
                st.metric("Ortalama Fiyat", f"₺{df_eh['price'].mean():.2f}")
            with col3:
                st.metric("En Düşük", f"₺{df_eh['price'].min():.2f}")
            with col4:
                st.metric("En Yüksek", f"₺{df_eh['price'].max():.2f}")
        else:
            st.info("ℹ️ English Home verisi yok")
    
    with tab4:
        st.subheader("📈 Fiyat Analizleri")
        
        if st.session_state.comparison_data is not None and len(st.session_state.comparison_data) > 0:
            df_comp = st.session_state.comparison_data
            
            # Fiyat karşılaştırma grafiği
            fig1 = go.Figure()
            
            fig1.add_trace(go.Bar(
                name='Madam Coco',
                x=df_comp.head(20)['madam_coco_product'],
                y=df_comp.head(20)['madam_coco_price'],
                marker_color='#667eea'
            ))
            
            fig1.add_trace(go.Bar(
                name='English Home',
                x=df_comp.head(20)['english_home_product'],
                y=df_comp.head(20)['english_home_price'],
                marker_color='#764ba2'
            ))
            
            fig1.update_layout(
                title="İlk 20 Ürün Fiyat Karşılaştırması",
                barmode='group',
                height=500
            )
            
            st.plotly_chart(fig1, use_container_width=True)
            
            # Fiyat farkı dağılımı
            fig2 = px.histogram(
                df_comp,
                x='price_difference_pct',
                nbins=30,
                title="Fiyat Farkı Dağılımı (%)",
                labels={'price_difference_pct': 'Fiyat Farkı (%)'}
            )
            fig2.update_traces(marker_color='#667eea')
            st.plotly_chart(fig2, use_container_width=True)
            
            # Hangi mağaza daha ucuz?
            cheaper_counts = df_comp['cheaper_at'].value_counts()
            fig3 = px.pie(
                values=cheaper_counts.values,
                names=cheaper_counts.index,
                title="Fiyat Avantajı Dağılımı",
                color_discrete_sequence=['#667eea', '#764ba2']
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        else:
            st.info("ℹ️ Grafik için veri yok")
    
    with tab5:
        st.subheader("📥 Veri Export")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.madamcoco_data is not None:
                csv_mc = st.session_state.madamcoco_data.to_csv(index=False, encoding='utf-8-sig')
                st.download_button(
                    "📥 Madam Coco Excel İndir",
                    csv_mc,
                    "madamcoco_products.csv",
                    "text/csv",
                    key='download-mc'
                )
        
        with col2:
            if st.session_state.englishhome_data is not None:
                csv_eh = st.session_state.englishhome_data.to_csv(index=False, encoding='utf-8-sig')
                st.download_button(
                    "📥 English Home Excel İndir",
                    csv_eh,
                    "englishhome_products.csv",
                    "text/csv",
                    key='download-eh'
                )
        
        if st.session_state.comparison_data is not None:
            csv_comp = st.session_state.comparison_data.to_csv(index=False, encoding='utf-8-sig')
            st.download_button(
                "📥 Karşılaştırma Raporu İndir",
                csv_comp,
                "price_comparison.csv",
                "text/csv",
                key='download-comp'
            )

else:
    # Başlangıç ekranı
    st.info("""
    ### 👋 Hoş Geldiniz!
    
    Bu sistem ile Madam Coco ve English Home mağazalarının fiyatlarını takip edebilir ve karşılaştırabilirsiniz.
    
    **Başlamak için:**
    1. Sol menüden "Otomatik Çekme" veya "Manuel Yükleme" seçin
    2. Verileri yükleyin
    3. "Analiz" sekmesine geçin
    
    **Özellikler:**
    - 🔄 Otomatik web scraping
    - 📊 Fiyat karşılaştırma
    - 📈 Detaylı analizler
    - 📥 Excel export
    """)

# Footer
st.markdown("---")
st.markdown("**Thorius Price Tracker** | Developed by Thorius Ltd © 2025")

import streamlit as st
import requests
import matplotlib.pyplot as plt
from collections import Counter

# FastAPI'nin URL'si
API_URL = "http://127.0.0.1:8000/predict"

st.title("Haber Kategorisi Tahmin Uygulaması")

# Kullanıcıdan metin girişi
news_texts = st.text_area("Birden fazla haber metni girin (her birini yeni satırda yazınız):")

# Tahmin butonu
if st.button("Tahmin Et"):
    if news_texts:
        # Metinleri satırlara ayıralım
        news_list = news_texts.split("\n")
        
        categories = []  # Kategorileri saklamak için liste
        
        # Her bir metni FastAPI'ye gönderip tahminleri alalım
        for news in news_list:
            if news.strip():  # Boş satırları atla
                response = requests.post(API_URL, json={"text": news.strip()})
                
                if response.status_code == 200:
                    prediction = response.json()
                    categories.append(prediction['category'])
                else:
                    st.error(f"'{news}' için tahmin yapılamadı.")
        
        if categories:
            # Kategorileri sayalım
            category_counts = Counter(categories)

            # Kategorilerin dağılımını görselleştirelim
            st.subheader("Kategori Dağılımı")
            fig, ax = plt.subplots()
            ax.bar(category_counts.keys(), category_counts.values(), color='skyblue')
            ax.set_xlabel('Kategori')
            ax.set_ylabel('Adet')
            ax.set_title('Her Kategorideki Haber Sayısı')
            st.pyplot(fig)

            # Kategorilerin detaylarını gösterelim
            st.subheader("Tahmin Edilen Kategoriler")
            for category, count in category_counts.items():
                st.write(f"{category}: {count} adet haber")
        else:
            st.warning("Hiçbir metin girilmedi.")
    else:
        st.warning("Lütfen haber metinlerini girin.")

# Haber Metinlerini Kategori Tahmini Projesi

Bu proje, haber metinlerini analiz ederek uygun kategorilere sınıflandıran bir makine öğrenimi modelini FastAPI ve Streamlit ile sunmaktadır. API üzerinden tahmin yapılabildiği gibi, kullanıcı dostu bir arayüzle de giriş yaparak tahmin sonucu alınabilir.

## Projeyi Başlatma Adımları

### 1. VS Code Üzerinden Projeyi Açın

Proje klasörünü Visual Studio Code ile açarak çalışmaya başlayabilirsiniz.

### 2. Sanal Ortamı Aktif Hale Getirin

Terminali açın ve proje dizininde aşağıdaki komutu girerek sanal ortamı etkinleştirin:

```
.\venv\Scripts\Activate
```

> Not: Eğer Unix/Linux/MacOS kullanıyorsanız:
>
> ```
> source venv/bin/activate
> ```

### 3. FastAPI Sunucusunu Başlatın

Aşağıdaki komutu kullanarak FastAPI sunucusunu başlatın:

```
cd app
uvicorn main:app --reload
```

Bu komut, `app.py` dosyasının bulunduğu dizinde çalıştırılmalıdır.

### 4. API'yi Tarayıcı Üzerinden Test Edin

Tarayıcınızda aşağıdaki adresi açın:

```
http://127.0.0.1:8000/docs
```

Bu sayfa, FastAPI tarafından otomatik olarak oluşturulan Swagger arayüzüdür.

* `/predict` endpoint’ini seçin.
* "Try it out" butonuna tıklayın.
* Test metinlerinden birini girin ve "Execute" butonuna basın.
* Tahmin sonucunu ekranda görebilirsiniz.

### 5. Streamlit Arayüzünü Başlatın

Yeni bir terminal penceresi açın ve aşağıdaki komutu girerek kullanıcı arayüzünü çalıştırın:

```
streamlit run app.py
```

Bu komut, Streamlit uygulamasını başlatarak varsayılan tarayıcıda aşağıdaki adreste arayüzü açacaktır:

```
http://localhost:8501
```

Buradan haber metinlerini girerek kategori tahminlerini görsel arayüz üzerinden test edebilirsiniz.

---

## Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki Python paketlerinin yüklü olması gerekir:

* fastapi
* uvicorn
* streamlit
* scikit-learn
* pandas
* joblib

Gereksinimleri yüklemek için:

```
pip install -r requirements.txt
```

---

## Lisans

Bu proje eğitim ve geliştirme amaçlıdır.

---

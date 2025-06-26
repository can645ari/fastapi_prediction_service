````markdown
# 📚 Haber Metinlerini Kategori Tahmini Projesi

Bu proje, haber metinlerini analiz ederek içeriklerine uygun kategori tahmini yapan bir makine öğrenmesi uygulamasıdır. Tahmin servisi hem **FastAPI** üzerinden REST API olarak hem de **Streamlit** üzerinden kullanıcı arayüzü ile kullanılabilir.

---

## Kurulum ve Çalıştırma Adımları

Aşağıdaki adımları izleyerek projeyi GitHub’dan bilgisayarınıza indirip çalıştırabilirsiniz.

---

### 1️⃣ Gerekli Kurulumlar

Aşağıdakilerin bilgisayarınızda kurulu olduğundan emin olun:

- [Git](https://git-scm.com/)
- [Python 3.7+](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/) (Tavsiye edilir)

Terminalden kontrol için:

```bash
git --version
python --version
````

---

### 2️⃣ Projeyi GitHub’dan Klonlayın

GitHub sayfasından bağlantıyı kopyalayın ve terminalde şu komutları çalıştırın:

```bash
git clone https://github.com/can645ari/fastapi_prediction_service.git
cd fastapi_prediction_service
```

---

### 3️⃣ Sanal Ortam Kurulumu

#### Sanal Ortam Oluşturun:

```bash
python -m venv venv
```

#### Sanal Ortamı Aktif Hale Getirin:

**Windows:**

```bash
.\venv\Scripts\activate
```

**MacOS / Linux:**

```bash
source venv/bin/activate
```

---

### 4️⃣ Gerekli Paketleri Yükleyin

Eğer `requirements.txt` dosyası varsa:

```bash
pip install -r requirements.txt
```

Eğer yoksa manuel olarak kurabilirsiniz:

```bash
pip install fastapi uvicorn streamlit scikit-learn pandas joblib
```

---

## 🧪 FastAPI Uygulamasını Çalıştırın

API sunucusunu başlatmak için:

```bash
cd app
uvicorn main:app --reload
```

Tarayıcınızda açın:

```
http://127.0.0.1:8000/docs
```

* `/predict` endpoint’ine gidin.
* “Try it out” butonuna tıklayın.
* Haber metnini girin ve “Execute” diyerek tahmini görün.

---

## 💻 Streamlit Arayüzünü Başlatın

Ana dizine dönerek şu komutu çalıştırın:

```bash
streamlit run app.py
```

Arayüz genellikle şu adreste açılır:

```
http://localhost:8501
```

Buradan haber metinleri girerek görsel arayüz üzerinden kategori tahmini yapabilirsiniz.

---

## 🔄 Güncellemeleri Alma (Opsiyonel)

Projeyi güncel tutmak için proje klasöründe şu komutu çalıştırabilirsiniz:

```bash
git pull
```

---

## 📋 Gereksinimler

* Python 3.7+
* FastAPI
* Uvicorn
* Streamlit
* Scikit-learn
* Pandas
* Joblib

---

## 📝 Lisans

Bu proje eğitim ve geliştirme amacıyla paylaşılmıştır.

---

## 📬 İletişim

Geliştirici: **Can Arı**
📧 E-posta: [caaan384@gmail.com](mailto:caaan384@gmail.com)

---

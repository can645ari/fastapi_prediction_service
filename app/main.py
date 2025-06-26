from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
import numpy as np

# FastAPI app nesnesi
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model ve vectorizer yüklemek
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'model', 'news_classifier_model.pkl')
vectorizer_path = os.path.join(current_dir, '..', 'model', 'tfidf_vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Giriş ve çıkış modelleri
class PredictionInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    category: str

# Servis başlangıç kontrolü
@app.get("/")
async def root():
    return {"message": "Prediction Service is running!"}

# Servisin çalışıp çalışmadığını test etmek için
@app.get("/ping")
async def ping():
    return {"ping": "pong!"}

# Tahmin endpoint
@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        # Giriş metnini vektörleştirmek için
        text_vector = vectorizer.transform([input_data.text])
        
        # Model ile tahmin yapmak
        prediction = model.predict(text_vector)
        
        # Tahmini döndürmek
        return PredictionOutput(category=prediction[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Model NLP multi bahasa untuk sentimen
# Menggunakan model multi bahasa untuk keakuratan analisa sentimen
MODEL_NAME = 'ClapAI/modernBERT-base-multilingual-sentiment'

def load_model_and_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    
    # Menggunakan device GPU jika ada, jika tidak ada maka menggunakan device CPU
    model.to(torch.device('cpu'))
    return tokenizer, model
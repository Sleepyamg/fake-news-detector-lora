# 📰 Fake News Detector with DistilBERT + LoRA (PEFT)

This project fine-tunes **DistilBERT** using **LoRA (PEFT)** for lightweight fake news classification.  
It includes training, evaluation, and a simple **FastAPI** deployment for real-time inference.

---

## 🚀 Features
- Uses **DistilBERT** as the base model.  
- **Parameter-Efficient Fine-Tuning (LoRA)** for faster training with fewer resources.  
- Achieves high accuracy on fake vs. real news classification.  
- **FastAPI REST API** for deployment.  
- Ready to run on **CPU or GPU** (Hugging Face + PyTorch).  

---

## 📂 Project Structure
```
├── notebooks/              # Jupyter notebooks for training & evaluation
├── fake_news_model/        # Saved model (tokenizer + LoRA adapters)
├── app/                    
│   ├── main.py             # FastAPI app for inference
│   └── requirements.txt    # Dependencies for deployment
└── README.md
```

---

## ⚙️ Installation

Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/fake-news-detector-lora.git
cd fake-news-detector-lora
```

Create a virtual environment and install dependencies:
```bash
pip install -r app/requirements.txt
```

Dependencies:
- transformers  
- datasets  
- torch  
- scikit-learn  
- peft  
- fastapi  
- uvicorn  

---

## 📊 Training

In Jupyter Notebook:
```bash
jupyter notebook notebooks/train.ipynb
```

After training, the model is saved in:
```
fake_news_model/
```

---

## 🧪 Evaluation

Run evaluation inside notebook:
```python
from sklearn.metrics import classification_report

y_pred = trainer.predict(dataset["test"])
print(classification_report(y_test, y_pred))
```

---

## 🚀 Deployment (FastAPI)

Run the API:
```bash
uvicorn app.main:app --reload
```

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/predict"      -H "Content-Type: application/json"      -d '{"text": "Breaking news: This is a fake headline"}'
```

### Example Response
```json
{
  "label": "fake",
  "score": 0.9987
}
```

---

## 📦 Export & Deployment

To deploy on free services like **Railway.app** or **Render**, push this repo to GitHub and connect it to the hosting platform.  
Make sure `requirements.txt` includes all dependencies.

---

## 🙌 Acknowledgements
- [Hugging Face Transformers](https://huggingface.co/transformers/)  
- [PEFT (LoRA)](https://huggingface.co/docs/peft/index)  
- [FastAPI](https://fastapi.tiangolo.com/)  

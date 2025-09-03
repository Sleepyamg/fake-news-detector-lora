from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import os

# Force Transformers to use PyTorch only
os.environ["TRANSFORMERS_NO_TF"] = "1"

app = FastAPI()

# Model path
model_path = "../fake_news_model"
a
# Load pipeline
pipe = pipeline("text-classification", model=model_path, tokenizer=model_path)

# Map HuggingFace labels to human-friendly names
label_map = {
    "LABEL_0": "real",
    "LABEL_1": "fake"
}

# Input schema
class InputText(BaseModel):
    text: str

@app.post("/predict")
async def predict(input: InputText):
    result = pipe(input.text)[0]  # Get first prediction
    friendly_label = label_map.get(result["label"], result["label"])
    return {
        "prediction": friendly_label,
        "confidence": round(result["score"], 4)
    }

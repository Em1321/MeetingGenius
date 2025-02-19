
# app/model.py
from transformers import pipeline

# Create a text-to-text generation pipeline using a summarization model.
# You can change the model to one that fits your needs.
model = pipeline("text2text-generation", model="facebook/bart-large-cnn")

def generate_summary_and_actions(prompt: str) -> str:
    response = model(prompt, max_new_tokens=200)
    return response[0]["generated_text"]
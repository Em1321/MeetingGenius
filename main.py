from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import uvicorn

# Define the request model
class TranscriptRequest(BaseModel):
    transcript: str

# Initialize the FastAPI app
app = FastAPI(title="Meeting Summarizer and Action Items Extractor API")

# Load the FLAN-T5-base model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_summary(transcript: str) -> str:
    """
    Generate a detailed summary of the given transcript.
    """
    prompt = (
        "Please provide a detailed summary of the following meeting transcript. "
        "Include key discussion points and decisions.\n\n"
        "Transcript: " + transcript + "\n\n"
        "Detailed Summary:"
    )
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        max_new_tokens=150,   # Increase if you want longer summary
        do_sample=True,
        temperature=0.9,
        num_beams=5,
        early_stopping=True
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary.strip()

def generate_action_items(transcript: str) -> str:
    """
    Extract a bullet list of action items from the meeting transcript.
    """
    prompt = (
        "Extract a bullet list of action items from the following meeting transcript. "
        "List each action item on a new line.\n\n"
        "Transcript: " + transcript + "\n\n"
        "Action Items:"
    )
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        max_new_tokens=100,   # Adjust for more detailed actions if needed
        do_sample=True,
        temperature=0.9,
        num_beams=5,
        early_stopping=True
    )
    actions = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return actions.strip()

@app.post("/summarize_actions")
async def summarize_and_extract(request: TranscriptRequest):
    try:
        summary = generate_summary(request.transcript)
        actions = generate_action_items(request.transcript)
        return {"summary": summary, "action_items": actions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

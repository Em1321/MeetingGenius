# app/summarizer.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model import generate_summary_and_actions

router = APIRouter()


class TranscriptRequest(BaseModel):
    transcript: str


@router.post("/")
async def summarize_meeting(request: TranscriptRequest):
    prompt = (
        "You are an assistant that summarizes meetings. Generate a concise summary and a list of action items from the transcript below.\n\n"
        "Transcript:\n"
        f"{request.transcript}\n\n"
        "Please output your response strictly in the following JSON format:\n"
        "{\n"
        '  "summary": "<summary text>",\n'
        '  "action_items": ["<item1>", "<item2>", ...]\n'
        "}\n\n"
        "Example output:\n"
        "{\n"
        '  "summary": "The team discussed the product launch, design feedback, marketing strategy, and production delays. Tasks were assigned and a follow-up meeting is scheduled.",\n'
        '  "action_items": [\n'
        '    "Sarah will refine the design based on feedback.",\n'
        '    "John will develop a revised marketing proposal.",\n'
        '    "Emily will follow up with suppliers regarding production delays."\n'
        "  ]\n"
        "}\n"
    )

    try:
        result = generate_summary_and_actions(prompt)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

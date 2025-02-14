# main.py
from fastapi import FastAPI
from app.summarizer import router as summarizer_router

app = FastAPI(title="Meeting Genius: Meeting Summarizer & Action Item Extractor API")

@app.get("/")
async def read_root():
    return {"message": "Welcome to MeetingGenius API! Visit /docs for API documentation."}

# Include the summarizer router under /summarize
app.include_router(summarizer_router, prefix="/summarize")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
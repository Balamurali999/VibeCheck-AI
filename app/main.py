from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.llm_service import get_vibe_analysis

app = FastAPI(title="VibeCheck AI Service")

# We define what the User must send us in their request
class VibeRequest(BaseModel):
    customer_comment: str
    draft_reply: str
    brand_voice: str
    model_name: str = "llama3.2:1b" # Default to the fastest model

@app.get("/")
def read_root():
    return {"status": "VibeCheck AI is Online", "hardware": "GTX 1650 Optimized"}

@app.post("/analyze")
async def analyze_vibe_endpoint(request: VibeRequest):
    try:
        # Call our logic layer
        result = get_vibe_analysis(
            customer_comment=request.customer_comment,
            draft_reply=request.draft_reply,
            brand_voice=request.brand_voice,
            model_name=request.model_name
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
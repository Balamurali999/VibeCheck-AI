from pydantic import BaseModel, Field
from typing import List

# This class defines the 'Vibe' of a single reply.
# It uses 'Field' to provide the LLM with hints on what we expect.
class VibeCheck(BaseModel):
    sentiment_score: int = Field(..., description="1-10 score: 1 is very angry, 10 is very happy.")
    sarcasm_detected: bool = Field(..., description="True if the user is being sarcastic.")
    tone_analysis: str = Field(..., description="One word: e.g., Professional, Aggressive, or Friendly.")
    brand_alignment: int = Field(..., description="1-10 score: how well the draft matches the target brand voice.")

# This is the 'Master Schema' that our API will return.
# It combines the analysis with the actual rewrites.
class VibeResponse(BaseModel):
    analysis: VibeCheck
    original_draft_quality: str = Field(..., description="A short 1-sentence critique of the original draft.")
    rewrites: List[str] = Field(
        ..., 
        min_items=3, 
        max_items=3, 
        description="Exactly 3 improved variations of the reply that match the brand voice."
    )
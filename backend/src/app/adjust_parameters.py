from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
current_threshold = 0.5  # Default threshold stored in memory

class FloatInput(BaseModel):
    threshold: float  # Ensure this matches the expected structure

@router.post("/")
async def adjust_emotion_threshold(input: FloatInput):
    global current_threshold
    if 0 <= input.threshold <= 1:  # Validate the threshold is within bounds
        current_threshold = input.threshold
        return {"message": "Threshold updated", "threshold": current_threshold}
    else:
        return {"error": "Threshold must be between 0 and 1"}
    # eventually will have different thresholds for different chunk segments

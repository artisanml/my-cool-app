"""Tiny FastAPI shell that serves a static Pomodoro single-page demo."""

from pathlib import Path
from typing import Literal

from fastapi import FastAPI, status
from fastapi.responses import FileResponse
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"

app = FastAPI(title="Pomodoro demo", description="Example static SPA behind FastAPI")


class SubscribeBody(BaseModel):
    tier: Literal["premium", "unlimited"]


PREMIUM_THANK_YOU = (
    "Congrats — you are now Prestige Tomato™ Elite. Money well spent. "
    "Your beanbag chair ships in 7–412 business fortnights."
)
UNLIMITED_THANK_YOU = (
    "Unlimited subscribed! Astronomers have renamed a minor moon after your receipt. "
    "Please do not invoice us ever again."
)


@app.get("/health")
async def health():
    """Simple readiness probe for demos and articles."""
    return {"status": "ok"}


@app.get("/")
async def index():
    return FileResponse(PUBLIC / "index.html")


THANK_YOU_MESSAGES = {
    "premium": PREMIUM_THANK_YOU,
    "unlimited": UNLIMITED_THANK_YOU,
}


@app.post("/subscribe", status_code=status.HTTP_201_CREATED)
async def subscribe(payload: SubscribeBody):
    """Silly fake billing — frontend calls this after the trial ends."""
    message = THANK_YOU_MESSAGES[payload.tier]
    return {"message": message}

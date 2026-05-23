"""Tiny FastAPI shell that serves a static Pomodoro single-page demo."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"

app = FastAPI(title="Pomodoro demo", description="Example static SPA behind FastAPI")


@app.get("/health")
async def health():
    """Simple readiness probe for demos and articles."""
    return {"status": "ok"}


@app.get("/")
async def index():
    return FileResponse(PUBLIC / "index.html")

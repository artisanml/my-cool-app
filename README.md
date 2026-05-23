# my-cool-app

Minimal FastAPI example that serves a single-page Pomodoro timer (plain HTML/CSS/JS) — handy for demos and articles.

## Run locally

```bash
cd my-cool-app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the Pomodoro UI and [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) for JSON health.

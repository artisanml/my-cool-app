# my-cool-app

Minimal FastAPI example that serves a single-page Pomodoro timer (plain HTML/CSS/JS) — handy for demos and articles. Use **Python 3.12+**.

## Run locally

```bash
cd my-cool-app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the Pomodoro UI and [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) for JSON health.

## Development checks

Install dev dependencies (pytest, coverage, linters):

```bash
pip install -r requirements-dev.txt
npm ci
```

Run the same checks CI uses locally:

```bash
ruff format --check .
ruff check .
npm run format:check
pytest
```

## Continuous Integration

Opening a pull request runs [`.github/workflows/ci.yml`](.github/workflows/ci.yml): Ruff lint/format on Python, Prettier `--check` on `public/`, and pytest with **100%** line + branch coverage on `main.py`.

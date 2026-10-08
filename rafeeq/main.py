from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from rafeeq.web.nav import NAV

WEB = Path(__file__).parent / "web"

app = FastAPI(title="Rafeeq")
app.mount("/static", StaticFiles(directory=WEB / "static"), name="static")
templates = Jinja2Templates(directory=WEB / "templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"nav": NAV, "active": "home"})


@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pathlib import Path

from .routers import anga

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(
    directory=str(BASE_PATH)+"/templates/", autoescape=False, auto_reload=True)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(anga.router, prefix='')


@app.exception_handler(404)
async def custom_404_handler(request, __):
    res = {"title": "Error Page",
           "error": "Page Not Found",
           "name": "Bebeto Nyamwamu"}
    return templates.TemplateResponse("404.html", {"request": request, "res": res})

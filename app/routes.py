from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

import requests, json

from app.config import Settings

settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

router = APIRouter()

@router.get("/")
def index(request: Request):
    query_params = dict(request.query_params)
    username = query_params.get("username")

    if username:
        return RedirectResponse(url=f"/{username}")

    return templates.TemplateResponse("main.html", {"request": request, "page_title": "GHTree | Search"})

@router.get("/{username}")
def index(request: Request, username: str):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return templates.TemplateResponse("404.html", {
            "request": request,
            "page_title": "GHTree | Not Found",
            "status_code": response.status_code,
            "text": "User not found",
            })

    data = response.json()

    if data.get("twitter_username"):
        data["twitter_url"] = f"https://twitter.com/{data.get('twitter_username')}"

    return templates.TemplateResponse("username.html", {
        "request": request, 
        "login": data.get("login"),
        "html_url": data.get("html_url"),
        "name": data.get("name"),
        "avatar_url": data.get("avatar_url"),
        "bio": data.get("bio"),
        "twitter": data.get("twitter_url"),
        "blog": data.get("blog"),
        "page_title": f"GHTree | {data.get('login')}",
        })
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

import requests, json, os

from app.config import Settings
from app.parse import parse_markdown

settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

router = APIRouter()
URL_REPO = "https://api.github.com/repos/rooyca/ghtree/contents/app/data"

@router.get("/")
def index(request: Request):
    query_params = dict(request.query_params)
    username = query_params.get("username")

    if username:
        return RedirectResponse(url=f"/{username}")

    return templates.TemplateResponse("main.html", {"request": request, "page_title": "GHTree | Search"})

@router.get("/v2/{username}")
def get_user_markdown(request: Request, username: str):
    # check if a file with username exists in repo
    try:
        response = requests.get(URL_REPO)
        data = response.json()
        for item in data:
            if item.get("name") == f"{username}.md":
                url = item.get("download_url")
                break
    except FileNotFoundError:
        return templates.TemplateResponse("404.html", {
            "request": request,
            "page_title": "GHTree | Not Found",
            "status_code": 404,
            "text": "NOPE",
            })
    parsed_data = parse_markdown(requests.get(url).text)

    return templates.TemplateResponse("v2_user.html", {
        "request": request,
        "profile_picture": parsed_data.get("profile_picture"),
        "username": parsed_data.get("username"),
        "pronouns": parsed_data.get("Pronouns"),
        "occupation": parsed_data.get("Occupation"),
        "location": parsed_data.get("Location"),
        "bio": parsed_data.get("bio"),
        "profile_items": parsed_data.get("profile_items"),
        "page_title": f"GHTree | {parsed_data.get('username')}",
        })

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
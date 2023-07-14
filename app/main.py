import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import Settings
from app.routes import router

settings = Settings()

templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yeld` on app shutdown.
    """

    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            str(settings.STATIC_DIR / "src" / "tw.css"),
            "-o",
            str(settings.STATIC_DIR / "css" / "main.css"),
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield


def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)

    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

    app.include_router(router)

    return app


app = get_app()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)

    if response.status_code == 404:
        return templates.TemplateResponse("404.html", {
            "request": request,
            "status_code": response.status_code,
            "text": "Page not found",
            "page_title": "GHTree | Not Found",
            })

    return response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

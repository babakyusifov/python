from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import aiohttp

app = FastAPI()

# Statik fayllar üçün qovluğu qeyd edirik
app.mount("/static", StaticFiles(directory="static"), name="static")

# index.html faylını kök route (/)-da göstəririk
@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Instagram username yoxlama funksiyası
async def check_username(username: str):
    url = f"https://www.instagram.com/{username}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 404:
                return {"status": "not_found", "message": f"Username '{username}' mövcud deyil."}
            elif response.status == 200:
                return {"status": "found", "message": f"Username '{username}' artıq istifadə olunur."}
            else:
                return {"status": "error", "message": "Xəta baş verdi, daha sonra yenidən yoxlayın."}

# Instagram username yoxlama API endpoint
@app.get("/check_username/{username}")
async def check(username: str):
    result = await check_username(username)
    return JSONResponse(content=result)

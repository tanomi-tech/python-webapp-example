from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
import os

app = FastAPI()
static_dir = 'static'

app.mount('/static', StaticFiles(directory=static_dir), name='static')
templates = Jinja2Templates(directory=static_dir)

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    # ฅ^._.^ฅ
    def get_cats(dir):
        files = os.listdir(dir)
        return [f"{request.url}{dir}/{image}" for image in files if os.path.isfile(f"{dir}/{image}")]
    random_cat = random.choice(get_cats(f"{static_dir}/images"))
    return templates.TemplateResponse(
        request=request, name="index.html", context={"cat": random_cat}
    )

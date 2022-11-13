from fastapi import FastAPI, Request
from settings import yandex_key, db
import requests

app = FastAPI()


@app.get("/get_address")
def accept_coords(request: Request):
    url = request.query_params
    link = f"https://geocode-maps.yandex.ru/1.x/?apikey={yandex_key}&format=json"
    for key, value in url.items():
        link += f'&{key}={value}'

    data = requests.get(link)
    try:
        data = data.json()
        db.setex(name=request, value=data, time=60 * 60)

        return data
    except:
        return {'Got Error!': 'oh..'}

# uvicorn main:app --reload

from fastapi import FastAPI, Request
import requests

app = FastAPI()
yandex_key = 'YOUR YANDEX KEY'


@app.get("/get_address")
def accept_coords(request: Request):
    url = request.query_params
    link = f"https://geocode-maps.yandex.ru/1.x/?apikey={yandex_key}&format=json"
    for key, value in url.items():
        link += f'&{key}={value}'

    data = requests.get(link)

    try:
        data = data.json()

        return data
    except:
        return {'Got Error!': 'oh..'}


@app.get("/items/{item_id}")
def accept(item_id: int, q):
    return {"item_id": item_id, "q": q}

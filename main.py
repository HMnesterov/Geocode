from fastapi import FastAPI
import requests
app = FastAPI()
yandex_key = '719cebe3-bb23-45a1-8bd7-8e4e1e5e8185'

@app.get("/get_address/{address}")
def accept_coords(address):
    link = f"https://geocode-maps.yandex.ru/1.x/?apikey={yandex_key}&geocode={address}"
    data = requests.get(link)
    data = data.json()
    return data


@app.get("/items/{item_id}")
def accept(item_id: int, q):
    return {"item_id": item_id, "q": q}
from fastapi import FastAPI
from app.data.deeds import data

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello, world!'}


@app.get('/deeds')
def deeds():
    return get_deeds()


def get_deeds():
    return data

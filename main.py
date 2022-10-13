from fastapi import FastAPI

import pickle
import lib
import pandas as pd
from schemas import PkRequest

app = FastAPI(title='Legendary Pokemon Prediction API',
              description = 'This API allows you to predict if a Pokemon is Legendary or not based on their stats.')

pickle_in = open("model.pkl","rb")

model = pickle.load(pickle_in)


@app.get('/')
async def index():
    return { "message" : "Hello World!" }


@app.post('/predictlegendary')
async def predict_legendary(request: PkRequest):
    request = request.dict()
    hitpoints = request['hitpoints']
    attack = request['attack']
    defense = request['defense']
    specattack= request['specattack']
    specdefense = request['specdefense']
    speed = request['speed']
    prediction = model.predict([[hitpoints,attack,defense,specattack,specdefense,speed]])
    if prediction[0] == 1:
        prediction_str = 'Pokemon is Legendary!'
    elif prediction[0] == 0:
        prediction_str = 'Pokemon is not Legendary :('
    return { 'prediction' : prediction_str }

import uvicorn

import pickle

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


origins = ['*']


app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers = ["*"],

)

class Music(BaseModel):

    Category: str

    Type: str

    Year: int

    Month: int



with open("mymodel.pkl", "rb") as f:
    model = pickle.load(f)

@app.get('/')

def index():

    return {'message': 'This is Mohammad Zahrawi'}

@app.post('/prediction')
def get_music_category(data: Music):

    received = data.dict()

    Category = received['Category']

    Type = received['Type']

    Year = received['Year']

    Month = received['Month']



    pred_name = model.predict([[Category, Type, Year, Month]]).tolist()[0]

    return {'prediction': pred_name}


print(model.predict([['Alkoholunfälle', 'insgesamt', 2020, 8]]))
from typing import Union
from fastapi import FastAPI
import current_date
import rand_checker
import requests
import json
from mangum import Mangum
from typing import List
app = FastAPI()

def return_response(message,statusCode):
    response = {
        "statusCode": statusCode,
        "body": {"message": message}
    }
    print(response)
    return response



@app.get("/")
def postping(): 
    return return_response("PONG!!!", 200)

@app.get("/ping")
def postping():
    return return_response("PONG!!!", 200)

@app.post('/sum')
def sum_num(numbers: List[int]):
    result = sum(numbers)
    return {'the sum of your numbers is': result}

@app.get("/alert")
def alert():
    return rand_checker.randAlert()

@app.get("/date")
def getdate():
    return {"The current date and time is": current_date.get_current_date()}

@app.get("/day")
def getday():
    return {"The current day is": current_date.get_current_day()}

@app.get("/version")
def getcheck():
    api = "https://api.github.com/repos/Ryujinx/release-channel-master/releases/latest"
    response_API = requests.get(api)
    return {"the current version of ryujinx is": response_API.json()["tag_name"]}


lambda_handler = Mangum(app, lifespan="off")

#lambda_handler(1, 2)
#uvicorn main:app --reload
from typing import Union
from fastapi import FastAPI
import current_date
import alert
import requests
import json
import ping
import check
from mangum import Mangum
import sum
from typing import List

def return_response(message,statusCode):
    response = {
        "statusCode": statusCode,
        "body": {"message": message}
    }
    print(response)
    return response


app = FastAPI()

@app.get("/")
def postping(): 
    response = ping.ping()
    return return_response(response, 200)

@app.get("/ping")
def postping():
    response = ping.ping()
    return return_response(response, 200)

@app.post('/sum')
def sum_num(numbers: List[int]):
    result = sum.sum_num(numbers)
    return return_response(result, 200)

@app.get("/alert")
def getalert():
    response= alert.randAlert()
    return return_response(response, 200)

@app.get("/date")
def getdate():
    response = current_date.getdate()
    return return_response(response, 200)

@app.get("/day")
def getday():    
    response = current_date.getday()
    return return_response(response, 200)

@app.get("/version")
def getcheck():
    response = check.version()
    return return_response(response, 200)


lambda_handler = Mangum(app, lifespan="off")


#uvicorn main:app --reload
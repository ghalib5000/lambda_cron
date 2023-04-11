#get current date
import datetime

def getdate():
    response = {"current_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M %p")}
    return response

def getday():
    response = {"current_day": datetime.datetime.now().strftime("%A")}
    return response


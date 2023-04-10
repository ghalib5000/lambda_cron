#get current date
import datetime
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M %p")
def get_current_day():
    return datetime.datetime.now().strftime("%A")

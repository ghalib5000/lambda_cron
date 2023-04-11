import random
def randAlert():
    number = random.random()
    number = round(number * 100)
    if number > 50:
        return {"Status":"ALERT!", "The value is": number}
    else:
        return {"Status":"OK", "The value is": number}
    
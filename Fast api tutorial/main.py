from fastapi import FastAPI

app = FastAPI()

@app.get("/")#home route
def home():
    return {"message":"Hi your are watching the home screen"}

@app.get("/about")
def about():
    return {"message":"About screen hi khede"}

@app.get("/kill")
def kill():
    return "I will kill the dark side of you"
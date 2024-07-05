from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return({"message":"Welcome to the Azure container world !"})

@app.get("/name")
def name():
    return({"name":"Shehzad Anjum"})
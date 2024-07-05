from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return({"message":"Hello world !"})

@app.get("/name")
def index():
    return({"name":"Shehzad Anjum"})



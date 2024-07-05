from fastapi import FastAPI

app = FastAPI()

app = FastAPI(title="AZURE Container -- Hello World ! Testing --", 
    version="0.0.2",
    # servers=[
    #     {
    #         "url": "http://127.0.0.1:8001", # ADD NGROK URL Here Before Creating GPT Action
    #         "description": "Development Server"
    #     }
    #     ]
    )


@app.get("/")
def index():
    return({"message":"Welcome to the Azure container world ! The final version"})

@app.get("/name")
def name():
    return({"name":"Shehzad Anjum"})

@app.get("/batch")
def batch():
    return({"batch":"36-37 Cloud computing and GenAI "})
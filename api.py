from fastapi import FastAPI
import os

app = FastAPI()


api_key = os.environ.get('API_KEY')

@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello World"}
    
@app.get("/hello")
async def hello():
    return {"message": "Hi, this is cicd, and api key is: " + api_key}

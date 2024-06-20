from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello World"}
    
MY_VARI = os.environ.get("API_KEY", "")
@app.get("/hello")
async def hello():
    return {"message": "Hi, this is cicd" + MY_VARI}

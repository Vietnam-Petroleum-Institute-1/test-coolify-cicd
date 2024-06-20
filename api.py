from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello World"}
    
@app.get("/hello")
async def hello():
    return {"message": "Hi, this is cicd"}

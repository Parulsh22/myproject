from fastapi import FastAPI

app = FastAPI()

# insatance of FastAPI
@app.get('/')
async def root():
    return {'message':'This is just fatsapi testing'}
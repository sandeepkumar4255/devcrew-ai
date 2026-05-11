from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Working Successfully"}


@app.get("/test")
def test():
    return {"status": "API Running"}
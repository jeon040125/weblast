from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return{"message": "hello bosma"}

@app.get("/home")
def home():
    return {"message":"home"}


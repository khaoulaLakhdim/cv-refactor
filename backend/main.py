from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app= FastAPI()

origins= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"],
)



@app.get("/")
def welcome():
    return {"message":"welcome to cv refactor app"}



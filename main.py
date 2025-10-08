from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Yoga backend is live and breathing 🧘‍♂️🔥"}
 

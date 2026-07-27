from fastapi import FastAPI

app = FastAPI(
    title="FixIT Manager",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to FixIT Manager API"
    }
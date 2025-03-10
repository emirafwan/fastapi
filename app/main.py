from fastapi import FastAPI

app = FastAPI(title="FastAPI App")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

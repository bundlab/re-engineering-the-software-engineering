from fastapi import FastAPI

app = FastAPI(title="order-service")

@app.get("/")
def read_root():
    return {
        "service": "order-service",
        "owner": "backend-core",
        "status": "active"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

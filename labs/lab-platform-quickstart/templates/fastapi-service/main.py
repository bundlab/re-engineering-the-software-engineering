from fastapi import FastAPI

app = FastAPI(title="{{SERVICE_NAME}}")

@app.get("/")
def read_root():
    return {
        "service": "{{SERVICE_NAME}}",
        "owner": "{{OWNER_TEAM}}",
        "status": "active"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

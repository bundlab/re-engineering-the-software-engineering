from fastapi import FastAPI

app = FastAPI(title="CI/CD Playground App")

@app.get("/")
def read_root():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

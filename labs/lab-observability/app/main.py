import time
import random
from fastapi import FastAPI, Response, HTTPException, status
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Observability Lab Service")

# Prometheus Metrics Definition
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests handled",
    ["method", "endpoint", "status_code"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["endpoint"]
)

@app.middleware("http")
async def monitor_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    endpoint = request.url.path
    status_code = str(response.status_code)
    
    REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, status_code=status_code).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
    
    return response

@app.get("/")
def read_root():
    # Simulate processing time between 10ms and 200ms
    time.sleep(random.uniform(0.01, 0.2))
    return {"message": "Observability service operational"}

@app.get("/error")
def trigger_error():
    if random.choice([True, False]):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Internal Server Error"
        )
    return {"message": "Success"}

@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

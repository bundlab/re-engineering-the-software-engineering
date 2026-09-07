# Lab: Hands-on Observability & Telemetry Verification

## Objective
Implement Prometheus metric instrumentation on a Python FastAPI application, configure metric scraping, and visualize HTTP request counters, error rates, and latency histograms using Grafana.

## Architecture
* **FastAPI App (`:8000`)**: Exposes `/metrics`, `/`, and `/error`.
* **Prometheus (`:9090`)**: Scrapes telemetry every 5 seconds.
* **Grafana (`:3000`)**: Visualizes real-time metric streams.

## Instructions

### 1. Launch the Stack
```bash
docker compose up --build -d
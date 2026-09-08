import os
import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Security Scanning Sandbox API")

# MOCK SECRET FOR DETECTION DEMO (DO NOT USE IN PRODUCTION)
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # gitleaks:allow

@app.get("/search")
def search_user(username: str):
    # Intentional SQL Injection vulnerability for SAST demonstration
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # BAD: String concatenation in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return {"users": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/ping")
def ping_host(host: str):
    # Intentional Command Injection vulnerability for SAST demonstration
    # BAD: Unsanitized input directly passed to OS shell execution
    response = os.system(f"ping -c 1 {host}")
    return {"status": response}
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade core pip tools before installing dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--cov=app", "--cov-report=term-missing"]
# STAGE 1: Install dependencies
FROM python:3.9 AS builder

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Create a minimal production image
FROM python:3.9-slim

WORKDIR /app

# Copy installed dependencies and binaries
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

EXPOSE 5000

# Use Gunicorn to start the Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

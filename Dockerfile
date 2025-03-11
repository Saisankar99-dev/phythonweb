# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY app.py .

# Copy built frontend assets directly into /app
COPY client/build/ .

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]

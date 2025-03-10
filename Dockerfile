# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files (backend and frontend)
COPY . .

# Assume that the frontend has been built into client/build.
# Create a static folder and copy the frontend build output into it.
RUN mkdir -p static && cp -r client/build/* static/

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]

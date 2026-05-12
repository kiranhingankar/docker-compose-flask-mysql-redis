# Use lightweight Python 3.11 image as base image
FROM python:3.11-slim

# Set working directory inside the container
# All commands will run from /app
WORKDIR /app

# Copy requirements file from local machine to container
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir reduces image size by avoiding cache storage
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Inform Docker that the container listens on port 5000
EXPOSE 5000

# Default command to start the Flask application
CMD ["python", "app.py"]

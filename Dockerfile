# Use an official Python runtime as a parent image
FROM python:3.12.5-slim

# Install necessary dependencies for pyautogui and Xvfb
RUN apt-get update && apt-get install -y \
    xvfb \
    libxkbcommon-x11-0 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable to prevent .pyc files from being written
ENV PYTHONDONTWRITEBYTECODE 1
# Set environment variable to buffer the Python output, ensuring logs are sent to Docker
ENV PYTHONUNBUFFERED 1

# Install Xvfb and set up the virtual display
RUN pip install --upgrade pip
RUN pip install pyautogui mouseinfo Flask

# Create app directory
WORKDIR /app

# Copy the rest of your application code
COPY . /app

# Expose port 5000 to the outside world
EXPOSE 5000

# Start Xvfb and Flask server
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & export DISPLAY=:99 && flask run --host=0.0.0.0"]

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    python3-dev \
    libpq-dev \
    netcat \
    curl

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Add and run as non-root user
RUN adduser --disabled-password --gecos '' myuser
USER myuser

# Run the application
CMD gunicorn app.wsgi:application --bind 0.0.0.0:8000
```

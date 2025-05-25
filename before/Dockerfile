# Secure Dockerfile using a minimal base image

FROM python:3.11-slim AS base

# Add a non-root user
RUN adduser --disabled-password --gecos '' appuser

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Drop privileges
RUN chown -R appuser:appuser /app
USER appuser

# Expose app port
EXPOSE 5000

# Add container health check
HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

# Run app
CMD ["python", "app.py"]
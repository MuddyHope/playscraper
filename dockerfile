# Use the official Playwright image for Python
FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install browser binaries
RUN playwright install --with-deps chromium

# Expose port for FastAPI
EXPOSE 8000

# Default command to run the API
CMD ["uvicorn", "api_service:app", "--host", "0.0.0.0", "--port", "8000"]

# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 4000

# Run the service with uvicorn
CMD ["uvicorn", "recipe_service:app", "--host", "0.0.0.0", "--port", "4000"]


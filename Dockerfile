# Use an official Python runtime as a parent image
FROM python:3.10-slim

ARG  API_KEY

ENV  API_KEY $API_KEY

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code into the container
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 8004

# Command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8004"]

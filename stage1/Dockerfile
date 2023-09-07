# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application code and requirements.txt into the container
COPY . .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Command to run your FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

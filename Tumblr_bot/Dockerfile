# Use the official Python image as the base image
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Copy .env file to the working directory
COPY .env .env
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 44777

# Define the command to run your application

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "44777"]


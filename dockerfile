# Use the official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /Kamm

# Copy the current directory's files into the container
COPY . .

# Command to run when the container starts
CMD ["python", "app.py"]
# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory

COPY app_page/ ./app_page

COPY run.py .

# Expose the port that the Flask app will run on
EXPOSE 80

# Set the entrypoint command to run the Flask app
# CMD ["python", "run.py"]
# CMD ["gunicorn", "-w", "4", "run:app"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "-w", "4", "run:app"]
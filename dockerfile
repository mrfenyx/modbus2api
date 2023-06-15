# Use an official Python runtime as a parent image
FROM python:3.9.17-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV MODBUS_HOST='192.168.2.11'
ENV MODBUS_PORT=502
ENV MODBUS_REGISTER=519

# Run app.py when the container launches
CMD [ "gunicorn", "-b", "0.0.0.0:80", "main:app" ]

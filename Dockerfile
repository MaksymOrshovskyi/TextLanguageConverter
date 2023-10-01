# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt (if you have one)
# RUN pip install -r requirements.txt

# Run the Python script
CMD ["python", "TextLanguageConverter.py"]

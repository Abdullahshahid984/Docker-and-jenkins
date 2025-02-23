# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install required system dependencies for LibreOffice
RUN apt-get update && apt-get install -y libreoffice

# Copy the application files into the container
COPY convert.py send_email.py ./
COPY network_cheatsheet.pdf ./

# Install Python dependencies if needed (e.g., smtplib does not require installation)
# You can add a requirements.txt if you have additional dependencies
# RUN pip install -r requirements.txt

# Set environment variables for email configuration
ENV EMAIL_SENDER=""
ENV EMAIL_PASSWORD=""
ENV EMAIL_RECEIVER=""

# Define the default command to run conversion and send email
CMD ["sh", "-c", "python convert.py && python send_email.py"]

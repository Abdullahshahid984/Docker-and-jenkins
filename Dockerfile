# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install required system dependencies for LibreOffice
RUN apt-get update && apt-get install -y libreoffice && rm -rf /var/lib/apt/lists/*

# Copy all available files into the container
# Set LibreOffice temporary directory to ensure writable permissions
ENV HOME=/app
COPY . /app/

# Set environment variables for email configuration
ENV EMAIL_SENDER=""
ENV EMAIL_PASSWORD=""
ENV EMAIL_RECEIVER=""

# Define the default command to run conversion and send email (if scripts exist)
CMD ["sh", "-c", "if [ -f convert.py ]; then python convert.py; fi && if [ -f send_email.py ]; then python send_email.py; fi"]

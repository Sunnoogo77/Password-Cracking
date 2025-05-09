# Use an official Python base image
FROM python:3.9

# Set a working directory inside the container
WORKDIR /app

# Copy all necessary files into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the GUI application (for PyQt5 support inside Docker)
ENV QT_X11_NO_MITSHM=1
ENV DISPLAY=:0

# Run the application
CMD ["python", "main.py"]

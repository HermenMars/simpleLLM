# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the source code
COPY src/ ./src/

# Set default command
CMD ["python", "src/main.py"]

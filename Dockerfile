# Use ROCm-ready PyTorch base image (supports AMD GPUs + CPU fallback)
FROM rocm/pytorch:latest

# Set work directory
WORKDIR /app

# Update apt packages and install tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy dependency list
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code
COPY src/ ./src/

# Default command to run
CMD ["python", "src/main.py"]

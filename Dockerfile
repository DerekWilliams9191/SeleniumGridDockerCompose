FROM ubuntu:latest

# Set non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    curl \
    gnupg \
    unzip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create Docker user with sudo privileges and no password
RUN useradd -m -d /home/docker -s /bin/bash docker && \
    echo "docker ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/docker && \
    chmod 0440 /etc/sudoers.d/docker

# Switch to Docker user
USER docker

# Create and activate virtual environment
RUN python3 -m venv /home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"

# Install python package
RUN python3 -m pip install selenium

# Copy code into container
WORKDIR /home/docker/
COPY . /home/docker/
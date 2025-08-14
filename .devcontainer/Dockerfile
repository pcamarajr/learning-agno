FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    curl \
    git \
    build-essential \
    zsh \
    && apt-get autoremove -y && apt-get clean -y

# Install Python development tools
RUN pip install --upgrade pip setuptools wheel

# Install Ollama client (Python)
RUN pip install ollama

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Copy requirements and install Python packages
COPY requirements.txt /tmp/pip-tmp/
RUN pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Set up workspace
WORKDIR /workspace

# Set zsh as default shell for the user
RUN chsh -s /usr/bin/zsh $USERNAME

# Configure git (optional, will use your host git config)
USER $USERNAME
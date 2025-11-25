# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Working directory inside the container
WORKDIR /app

# Copy only dependency files first (for better Docker caching)
COPY pyproject.toml ./

# Install build tools and dev dependencies (from pyproject extras)
# Using setuptools backend compatible with install -e .[dev]
RUN pip install --upgrade pip setuptools wheel

# Copy the rest of your source code
COPY . .

# Install your package in editable mode with dev extras
RUN pip install -e .[dev]

# Optionally run lint/typecheck/tests as part of build (uncomment if desired)
# RUN make lint-check
# RUN make typecheck
# RUN make test

# Default command: run your project’s entry module
# Replace `{{ cookiecutter.package_name }}` with actual generated package name
CMD ["python", "-m", "{{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}"]

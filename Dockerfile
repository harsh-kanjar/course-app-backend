# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /code/

# Collect static files (if you have STATIC_ROOT configured)
RUN python manage.py collectstatic --noinput

# Apply database migrations (optional, you can also do this manually)
RUN python manage.py migrate --noinput

# Install Gunicorn
RUN pip install gunicorn

# Run Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "yourproject.wsgi:application"]

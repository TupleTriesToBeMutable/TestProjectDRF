FROM python:3.11.9

# Set PYTHONUNBUFFERED for immediate output
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8000
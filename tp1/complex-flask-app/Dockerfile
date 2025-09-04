FROM python:3.11-slim

WORKDIR /app

COPY app.py /app

# Installer Flask et PyMongo
RUN pip install flask pymongo

EXPOSE 5000

CMD ["python", "app.py"]
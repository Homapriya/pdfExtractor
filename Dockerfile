FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY extractor.py .

RUN mkdir -p /app/input /app/output

ENTRYPOINT ["python", "extractor.py"]

FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY data_reader.py /app/
COPY main.py /app/
COPY producer.py /app/

EXPOSE 6005

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6005"]
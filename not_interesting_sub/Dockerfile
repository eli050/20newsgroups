FROM python:3.13-slim

WORKDIR /app

COPY /not_interesting_sub/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /not_interesting_sub /app/not_interesting_sub

COPY /subscribers /app/subscribers

EXPOSE 8002

CMD ["uvicorn", "not_interesting_sub.main:app", "--host", "0.0.0.0", "--port", "8002"]
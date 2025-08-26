FROM python:3.13-slim

WORKDIR /app

COPY /interesting_sub/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /interesting_sub /app/interesting_sub

COPY /subscribers /app/subscribers

EXPOSE 8001

CMD ["uvicorn", "interesting_sub.main:app", "--host", "0.0.0.0", "--port", "8001"]
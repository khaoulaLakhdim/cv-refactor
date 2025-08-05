FROM python:3.11-slim

WORKDIR /usr/src/app

COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]



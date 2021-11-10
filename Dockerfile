FROM python:3.9.7-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["gunicorn"]
CMD ["--workers=3", "--bind=0.0.0.0:5000", "wsgi:app"]
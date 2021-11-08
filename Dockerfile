FROM python:3.9.7-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0", "--port=80"]

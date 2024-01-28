FROM python:3.11
LABEL authors=["SEBASTIAN","ALEKSANDRA"]

ENV PYTHONUNBUFFERED=1

WORKDIR /App

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

FROM mysql:8

ENV MYSQL_ROOT_PASSWORD pass
COPY ./data.sql /docker-entrypoint.initdb.d/data.sql
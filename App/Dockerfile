FROM python:3.11
LABEL authors=["SEBASTIAN","ALEKSANDRA"]

ENV PYTHONUNBUFFERED=1

WORKDIR /App

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY App /app/App/

COPY . .

EXPOSE 8000

RUN ["sh", "-c", "python manage.py makemigrations"]

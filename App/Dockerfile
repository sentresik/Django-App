FROM python:3.11
LABEL authors=["SEBASTIAN","ALEKSANDRA"]

ENV PYTHONUNBUFERRED=1

WORKDIR /Project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver"]
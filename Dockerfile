FROM python:3.9.0-slim-buster

COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD [ "python3","manage.py","runserver", "0.0.0.0:8000"]


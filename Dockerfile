FROM python:3

WORKDIR /usr/src/contactsGenerator

COPY . ./

RUN pip install -r requirements.txt

CMD exec gunicorn --bind:$PORT --workers 1 --threads 8 --timeout 0 app:app

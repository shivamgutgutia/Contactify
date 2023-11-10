FROM python:3.11.5

WORKDIR /usr/src/contactsGenerator

COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3" ,"app.py"]


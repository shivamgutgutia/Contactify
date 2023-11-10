FROM ubuntu

RUN apt update
RUN apt install python3-pip -y

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app/
EXPOSE 5000
CMD ["python3","app.py"]


FROM python:3.10.0-alpine

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
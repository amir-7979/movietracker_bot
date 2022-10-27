FROM python:3.10.6

WORKDIR /code

COPY ./api_requests /code/api_requests
COPY ./model /code/model
COPY ./utilities /code/utilities
COPY ./view_model /code/view_model
COPY ./requirements.txt /code/requirements.txt
COPY ./main.py /code/main.py
COPY ./bot2.session /code/bot2.session
COPY ./movie_tracker.db /code/movie_tracker.db


RUN pip3 install --no-cache-dir --upgrade -r requirements.txt


CMD ["python", "./main.py"]
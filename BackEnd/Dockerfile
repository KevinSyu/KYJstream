FROM python:3.9.0

ENV ENVIRONMENT dockerdev

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ./libs/ /app/libs/
RUN pip install ./libs/

COPY . /app

CMD python main.py 
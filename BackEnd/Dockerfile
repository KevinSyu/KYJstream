FROM python:3.9.0

ENV ENVIRONMENT dockerdev

WORKDIR /app

# ADD requirements.txt /app
ADD . /app

RUN pip install -r requirements.txt
RUN pip install ./libs/

CMD python main.py 
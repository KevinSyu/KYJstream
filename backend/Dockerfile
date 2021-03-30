FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app/
ENV FLASK_APP hello.py
ENV FLASK_ENV development
CMD flask run --host=0.0.0.0
 
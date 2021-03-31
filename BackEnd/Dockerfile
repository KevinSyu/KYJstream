FROM python:3.9.0

WORKDIR /app

# ADD requirements.txt /app
ADD . /app

RUN  python  ./libs/setup.py install
RUN    pip install -r requirements.txt

CMD python main.py
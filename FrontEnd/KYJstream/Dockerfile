FROM node:14.15

RUN mkdir /app
WORKDIR /app

RUN npm install -g @angular/cli@11.0.7

COPY ./package.json /app
RUN npm install

COPY . /app
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll"]
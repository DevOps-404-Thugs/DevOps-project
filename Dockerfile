FROM python:3

RUN apt-get update
RUN apt-get install -y nodejs npm
RUN npm install -g yarn

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /user/src/app

RUN pip3 install -r /user/src/app/requirements.txt

RUN cd /user/src/app/front; yarn build

RUN cd /user/src/app/source; ./local.sh

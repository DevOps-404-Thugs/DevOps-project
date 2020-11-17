FROM python:3

RUN apt-get update
RUN apt-get install -y nodejs npm
RUN npm install -g yarn

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /user/src/app

RUN cd /user/src/app; pip3 install -r requirements.txt

RUN cd /user/src/app/front; yarn build

CMD ["python3",  "/user/src/app/source/endpoints.py"]

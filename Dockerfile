FROM python:3

RUN apt-get update
RUN apt-get install -y nodejs npm
RUN npm install -g yarn

WORKDIR /app

COPY . /app

RUN cd /app; make dev_env

RUN cd /app; make build_front

WORKDIR /app/source

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["endpoints.py"]
<<<<<<< HEAD
FROM node:20-bullseye-slim
=======
FROM docker.io/node:22-bookworm-slim
>>>>>>> master

WORKDIR /app

COPY ./package.json /app

RUN npm install && npm cache clean --force

ENV PATH=./node_modules/.bin/:$PATH

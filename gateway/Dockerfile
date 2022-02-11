FROM node:16-alpine

WORKDIR /app

ENV PRODUCTION=1

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000


CMD [ "node", "index.js" ]

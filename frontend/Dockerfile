FROM node:14.15.0

EXPOSE 3000

WORKDIR /usr/src/app

COPY . .

RUN npm install -g react-scripts
RUN npm install --force

CMD ["npm", "start"]
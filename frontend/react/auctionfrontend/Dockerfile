# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /auctionfronted

# add to $PATH
ENV PATH /node_modules/.bin:$PATH

# install app dependencies
COPY /package.json ./
COPY /package-lock.json ./
RUN npm install --silent

# add app
COPY . ./

# start app
CMD ["npm", "start"]

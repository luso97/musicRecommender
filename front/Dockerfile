FROM node:12-alpine as builder

RUN mkdir app

WORKDIR /app

COPY MusicRecom/package.json MusicRecom/package-lock.json /app/MusicRecom/

RUN npm install --prefix MusicRecom

# Copy app files.
COPY MusicRecom /app/MusicRecom/

# Build app
RUN npm run build --prefix MusicRecom -- --output-path=./dist/out

FROM nginx:1.15.7-alpine

EXPOSE 8080

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/MusicRecom/dist/out /usr/share/nginx/html

COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
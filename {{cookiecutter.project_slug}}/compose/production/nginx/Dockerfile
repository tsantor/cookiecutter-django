FROM docker.io/nginx:1.17.8-alpine

COPY ./compose/production/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./compose/production/nginx/default.conf /etc/nginx/conf.d/default.conf

# COPY ./compose/production/nginx/.htpasswd /etc/nginx/.htpasswd

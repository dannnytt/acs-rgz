FROM nginx:latest

COPY certs /etc/nginx/certs
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]

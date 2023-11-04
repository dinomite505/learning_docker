FROM nginx:1.23

# copies nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

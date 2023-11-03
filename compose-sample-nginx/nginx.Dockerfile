FROM nginx:1.25

# copies nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

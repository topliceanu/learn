FROM ubuntu

RUN apt-get update && apt-get install -y iputils-ping traceroute apache2

EXPOSE 80

ENTRYPOINT ["apache2ctl"]
CMD ["-D", "FOREGROUND"]

FROM phusion/baseimage

# add code and directories
RUN mkdir /mymdb
WORKDIR /mymdb
COPY requirements* /mymdb/
COPY django / /mymdb/django
COPY scripts/ /mymdb/scripts
RUN mkdir /var/log/mymdb/
RUN touch /var/log/mymdb/mymdb.log

RUN apt -y update
RUN apt install -y \
    nginx \
    postgresql-client \
    python3.7
    python3.7-pip
RUN pip3 install virtualenv
RUN virtual env /mymdb/venv
RUN bash /mymdb/scripts/pip_install.sh /mymdb

# collect the static files
RUN bash /mymdb/scripts/collect_static.sh /mymdb

COPY nginx/mymdb.conf /etc/nginx/sites-available/mymdb.conf
RUN rm /etc/nginx/sites-enables/*
RUN ln -s /etc/nginx/sites-available/mymdb.conf /etc/nginx/sites-enabled/mymdb.conf

COPY runit/nginx /etc/service/nginx
RUN chmod +x /etc/service/nginx/run

# configure uwsgi
COPY uwsgi/mymdb.ini /etc/uwsgi/apps-enabled/mymdb.ini
RUN mkdir -p /var/log/uwsgi/
RUN touch /var/log/uwsgi/
RUN chown www-data /var/log/uwsgi/mymdb.log
RUN chown www-data /var/log/mymdb/mymdb.log

COPY runit/uwsgi /etc/service/uwsgi
RUN chmod +x /etc/service/uwsgi/run

RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp*

EXPOSE 80

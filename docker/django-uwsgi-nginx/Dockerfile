FROM ubuntu:16.04

MAINTAINER Dockerfiles


# 安装git、python、nginx、supervisor等，并清理缓存

RUN apt-get update && \
    apt-get upgrade -y && \ 
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	libmysqlclient-dev && \
        pip3 install --upgrade -i https://pypi.doubanio.com/simple/ pip setuptools && \
  	rm -rf /var/lib/apt/lists/*

RUN pip3 install -i https://pypi.doubanio.com/simple/ uwsgi
 
 
# 环境变量

ENV MYSQL_DATABASE_NAME sanhui
# ENV EMAIL_HOST_USER myemail@email.com
# ENV EMAIL_HOST_PASSWORD my-secret-password


# nginx、supervisor配置

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/


# 安装项目所需python第三方库

COPY requirements.txt /home/docker/code/SanHui/
RUN pip install -i https://pypi.doubanio.com/simple/ -r /home/docker/code/SanHui/requirements.txt


# uwsgi.ini 及 uwsgi_params

COPY . /home/docker/code/


EXPOSE 80
CMD ["supervisord", "-n"]

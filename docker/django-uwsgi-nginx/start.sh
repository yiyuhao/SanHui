#!/bin/bash

# 镜像不存在时创建镜像
if ! docker images | grep sanhui; then
    echo 'The docker image does not exist,'
    echo 'Now creating image <sanhui>...'
    docker build -t sanhui $(pwd)
fi

# 镜像存在时，检查容器是否存在
if docker ps -a | grep -i sanhui; then
    # 容器存在时则删除容器
    echo 'The docker container <sanhui> already exist, deleting it...'
    docker rm -f webapp-sanhui
    # 启动容器
    docker run -itd \
               --link mysql:mysql \
               -v /root/git_repo/SanHui/:/home/docker/code/SanHui \
               --name webapp-sanhui \
               -p 80:80 \
           sanhui
else
    # 第一次创建容器时需要更新数据库
    docker run -itd \
               --link mysql:mysql \
               -v /root/git_repo/SanHui/:/home/docker/code/SanHui \
               --name webapp-sanhui \
               -p 80:80 \
           sanhui \
           sh -c 'python /home/docker/code/SanHui/manage.py migrate && supervisord -n'
fi

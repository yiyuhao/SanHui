#!/bin/bash 

# 镜像存在时，检查容器是否存在
if docker ps -a | grep -i mysql-sanhui; then
    # 容器存在时则删除容器
    echo 'The docker container <mysql-sanhui> already exist, deleting it...'
    docker rm -f mysql-sanhui
fi

echo "creating a mysql container.."
docker run -d --name mysql-sanhui \
           -v $(pwd)/conf.d:/etc/mysql/conf.d \
           -v $(pwd)/data:/var/lib/mysql \
           -e MYSQL_ROOT_PASSWORD="huawei@123" \
           -e MYSQL_DATABASE="sanhui" \
           -P \
       mysql:5.7.19 \
           --character-set-server=utf8 --collation-server=utf8_general_ci


FROM jenkins/jenkins:lts

USER root

WORKDIR /var/jenkins_home/workspace

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    docker.io \
    docker-compose \
    && rm -rf /var/lib/apt/lists/*



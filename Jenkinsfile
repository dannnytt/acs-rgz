pipeline {
    agent any

    environment {
        SERVICE_NAME = 'app'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Клонирование репозитория') {
            steps {
                git branch: 'main', url: 'https://github.com/dannnytt/acs-rgz'
            }
        }

        stage('Сборка Docker-образа') {
            steps {
                script {
                    echo "Сборка нового Docker-образа..."
                    sh """
                        docker-compose -f ${DOCKER_COMPOSE_FILE} build ${SERVICE_NAME}
                    """
                }
            }
        }

        stage('Перезапуск Flask-приложения') {
            steps {
                script {
                    def containerExists = sh(
                        script: "docker ps -aq -f name=flask-container",
                        returnStatus: true
                    ) == 0

                    if (containerExists) {
                        echo "Контейнер flask-container уже существует. Удаляем его..."
                        sh """
                            docker stop flask-container || true
                            docker rm -f flask-container || true
                        """
                    }

                    echo "Запуск нового контейнера..."
                    sh """
                        docker-compose -f ${DOCKER_COMPOSE_FILE} up -d ${SERVICE_NAME}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Обновление Flask-приложения завершено успешно!"
        }
        failure {
            echo "Развертывание завершилось с ошибками. Проверьте логи."
        }
    }
}

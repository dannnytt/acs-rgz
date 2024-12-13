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
                    echo "Остановка старого контейнера..."
                    sh """
                        docker-compose -f ${DOCKER_COMPOSE_FILE} stop ${SERVICE_NAME}
                        docker-compose -f ${DOCKER_COMPOSE_FILE} rm -f ${SERVICE_NAME}
                    """
                    
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

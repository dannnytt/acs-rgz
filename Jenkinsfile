pipeline {
    agent any

    environment {
        SERVICE_NAME = 'app'
        CONTAINER_NAME = 'flask-app'
    }

    stages {
        stage('Клонирование репозитория') {
            steps {
                git branch: 'main', url: 'https://github.com/dannnytt/acs-rgz'
            }
        }

        stage('Сборка изображения') {
            steps {
                script {
                    sh """
                        docker-compose build ${SERVICE_NAME}
                    """
                }
            }
        }

        stage('Развертывание контейнера') {
            steps {
                script {
                    try {
                        // Удаление всех старых контейнеров, связанных с сервисом app
                        def containers = sh(script: 'docker ps -aqf "name=flask-container"', returnStdout: true).trim().split("\n")
                        containers.each {
                            sh "docker rm -f ${it}"
                        }

                        // Удаление всех ресурсов сервиса
                        sh """
                            docker-compose down --rmi all --volumes ${SERVICE_NAME} || echo 'Не удалось удалить контейнеры'
                        """
                    } catch (Exception e) {
                        error "Ошибка при остановке и удалении контейнеров: ${e.message}"
                    }

                    // Перезапуск сервиса
                    sh """
                        docker-compose up -d ${SERVICE_NAME}
                    """
                }
            }
        }
    }
}

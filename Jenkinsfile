pipeline {
    agent any

    environment {
        SERVICE_NAME = 'app'
        CONTAINER_NAME = 'flask-container'
        IMAGE_NAME = 'flask_app-image:latest'
        DOCKERFILE_PATH = './app'
        APP_PORT = '5000'
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
                    echo "Проверка и удаление старого образа, если существует..."
                    def isImageExist = sh(script: "docker images -q ${IMAGE_NAME}", returnStdout: true).trim()
                    if (isImageExist) {
                        sh "docker rmi -f ${IMAGE_NAME} || true"
                    }

                    echo "Сборка нового Docker-образа..."
                    sh "docker build -t ${IMAGE_NAME} ${DOCKERFILE_PATH}"
                }
            }
        }

        stage('Развертывание Docker-контейнера') {
            steps {
                script {
                    echo "Проверка запущенного контейнера..."
                    def isRunning = sh(script: "docker ps -q -f name=${CONTAINER_NAME}", returnStdout: true).trim()
                    if (isRunning) {
                        echo "Остановка и удаление старого контейнера..."
                        sh "docker stop ${CONTAINER_NAME} || true"
                        sh "docker rm -f ${CONTAINER_NAME} || true"
                    }

                    echo "Удаление неиспользуемых Docker volumes..."
                    sh "docker volume prune -f || true"

                    echo "Запуск нового контейнера..."
                    sh """
                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            -p ${APP_PORT}:${APP_PORT} \
                            ${IMAGE_NAME}
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Очистка временных файлов завершена."
        }
        success {
            echo "Развертывание завершено успешно!"
        }
        failure {
            echo "Развертывание завершилось с ошибками. Проверьте логи."
        }
    }
}

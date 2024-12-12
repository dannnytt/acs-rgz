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

        stage('Развертывание контейнера') {
            steps {
                script {
                    try {
                        def isRunning = sh(script: "docker ps -q -f name=${CONTAINER_NAME}", returnStdout: true).trim()

                        if (isRunning) {
                            sh "docker stop ${CONTAINER_NAME}"
                            sh "docker rm ${CONTAINER_NAME}"
                        }

                        sh "docker-compose down ${SERVICE_NAME}"
                        sh "docker-compose up --build -d ${SERVICE_NAME}"

                    } catch (Exception e) {
                        error "Ошибка при развертывании контейнера: ${e.message}"
                    }
                }
            }
        }
    }
}

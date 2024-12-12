pipeline {
    agent any

    environment {
        SERVICE_NAME = 'app'
        CONTAINER_NAME = 'flask-app'
        IMAGE_NAME = 'flask_app-image:latest'
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
                            sh "docker stop ${CONTAINER_NAME} || true"
                            sh "docker rm ${CONTAINER_NAME} || true"
                        }

                        def isImageExist = sh(script: "docker images -q ${IMAGE_NAME}", returnStdout: true).trim()
                        if (isImageExist) {
                            sh "docker rmi ${IMAGE_NAME} || true"
                        }

                        sh "docker volume ls -qf dangling=true | xargs -r docker volume rm || true"
                        sh "docker-compose down || true"
                        sh "docker-compose up --build -d ${SERVICE_NAME}"

                    } catch (Exception e) {
                        error "Ошибка при развертывании контейнера: ${e.message}"
                    }
                }
            }
        }
    }
}

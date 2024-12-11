pipeline {
    agent any
    
    environment {
        SERVICE_NAME='app'
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
                        sh """
                            docker-compose stop ${SERVICE_NAME} || echo 'Сервис ${SERVICE_NAME} не запущен. Продолжение...'
                            docker-compose rm ${SERVICE_NAME} || echo 'Контейнер ${SERVICE_NAME} не найден. Продолжение...'
                        """
                    } catch (Exception e) {
                        error "Ошибка при остановке и удалении контейнера ${SERVICE_NAME}: ${e.message}"
                    }

                    sh """
                        docker-compose up -d ${SERVICE_NAME}
                    """
                }
            }
        }
    }
}
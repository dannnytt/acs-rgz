pipeline {
    agent any
    
    environment {
        SERVICE_NAME='app'
    }
    
    stages {
        stage('Клонирование репозитория') {
            steps {
                git branch: 'main', url: 'https://gitlab.com/sibsutis-repo/sibsutis-labs/acs-rgz'
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
                    sh """
                        docker-compose stop ${SERVICE_NAME} || echo 'Сервис ${SERVICE_NAME} не запущен. Продолжение...'
                        docker-compose rm -f ${SERVICE_NAME} || echo 'Контейнер ${SERVICE_NAME} не найден. Продолжение...'
                    """
                
                    sh """
                        docker-compose up -d ${SERVICE_NAME}
                    """
                }
            }
        }
    }
}
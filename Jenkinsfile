pipeline {
    agent any
    
    environment {
        SERVICE_NAME='app'
        CONTAINER_NAME='flask-app'
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
                            docker-compose down --rmi all --volumes --remove-orphans ${SERVICE_NAME}
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
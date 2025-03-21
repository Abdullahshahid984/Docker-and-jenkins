pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jenkins'
        CONTAINER_NAME = 'word-to-pdf-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/word-to-pdf.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'email-credentials', usernameVariable: 'EMAIL_SENDER', passwordVariable: 'EMAIL_PASSWORD')]) {
                        sh '''
                            docker run --rm \
                              -v "$(pwd):/app" \
                              -e EMAIL_SENDER="$EMAIL_SENDER" \
                              -e EMAIL_RECEIVER="$EMAIL_SENDER" \
                              ${IMAGE_NAME}
                        '''
                    }
                }
            }
        }
    }
}

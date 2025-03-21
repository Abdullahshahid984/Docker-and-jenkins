pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Abdullahshahid984/docker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'email-credentials', usernameVariable: 'EMAIL_SENDER', passwordVariable: 'EMAIL_PASSWORD')]) {
                        sh """
                            docker run --rm \
                              -e EMAIL_SENDER="${EMAIL_SENDER}" \
                              -e EMAIL_RECEIVER="${EMAIL_SENDER}" \
                              ${IMAGE_NAME}
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Email sent successfully!"
        }
        failure {
            echo "❌ Email sending failed!"
        }
    }
}

pipeline {
    agent any

    environment {
        IMAGE_NAME = "word-to-pdf"
        CONTAINER_NAME = "word-to-pdf-container"
        WORKSPACE_DIR = "${WORKSPACE}"
        PDF_FILE = "converted.pdf"  // Change this to your actual PDF output file name
        EMAIL_TO = "abdullahshahid984@gmail.com"  // Change to the actual recipient's email
        EMAIL_SUBJECT = "Converted PDF File"
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
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Run Docker Container and Convert PDF') {
            steps {
                script {
                    sh 'docker run --rm -v ${WORKSPACE_DIR}:/app ${IMAGE_NAME}'
                }
            }
        }

        stage('Send Email with PDF') {
            steps {
                script {
                    emailext (
                        to: "${EMAIL_TO}",
                        subject: "${EMAIL_SUBJECT}",
                        body: "The converted PDF is attached.",
                        attachFiles: "${WORKSPACE_DIR}/${PDF_FILE}"
                    )
                }
            }
        }
    }
}

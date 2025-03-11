pipeline {
    agent any  // Run directly on the host

    environment {
        DOCKER_REGISTRY = 'docker.io'  // Docker Hub
        DOCKER_USER = 'saisankar99'    // Your Docker Hub username
        APP_IMAGE = "${DOCKER_USER}/my-python-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Saisankar99-dev/phythonweb'
            }
        }

        stage('Build Frontend') {
            steps {
                dir('client') {
                    sh 'npm install --loglevel verbose'
                    sh 'npm run build'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${APP_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-registry-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u "$DOCKER_USER" --password-stdin'
                    sh "docker push ${APP_IMAGE}"
                }
            }
        }

        stage('Deploy') {
            steps {
                sh "docker run -d -p 5000:5000 ${APP_IMAGE}"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}


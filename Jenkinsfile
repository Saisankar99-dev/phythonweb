// Jenkinsfile
pipeline {
    // Use the custom Docker agent defined in Dockerfile.agent
    agent {
        docker {
            image 'my-custom-agent:latest'
            // Mount the host Docker socket so Docker commands work inside the container
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    environment {
        // Define your Docker registry and image name (adjust as needed)
        DOCKER_REGISTRY = 'saisankr99'
        APP_IMAGE = "${DOCKER_REGISTRY}/my-python-app:latest"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from your repository
                checkout scm
            }
        }
        
        
        
        stage('Build Frontend') {
            steps {
                // Change directory to the frontend code and build it
                dir('client') {
                    // Install dependencies from package.json
                    sh 'npm install'
                    // Build the React application (creates the build folder)
                    sh 'npm run build'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build the Docker image for the application using the Dockerfile
                sh "docker build -t ${APP_IMAGE} ."
            }
        }
        
        stage('Push Docker Image') {
            steps {
                // Use Jenkins credentials to securely log in to the Docker registry and push the image
                withCredentials([usernamePassword(credentialsId: 'docker-registry-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login ${DOCKER_REGISTRY} -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                    sh "docker push ${APP_IMAGE}"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the application by running the container on the host
                sh "docker run -d -p 5000:5000 ${APP_IMAGE}"
            }
        }
    }
    
    post {
        always {
            // Clean up the workspace to avoid polluting future builds
            cleanWs()
        }
    }
}

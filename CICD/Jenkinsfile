pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vamshiadep21/mlops-infer'
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning the repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}:${TAG}"
                sh "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${TAG}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Minikube Kubernetes Cluster...'

                sh """
                    sed -i 's|image: .*|image: ${IMAGE_NAME}:${TAG}|' k8s/deployment.yaml
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl rollout status deployment/mlops-infer-deployment
                """
            }
        }

        stage('Access App') {
            steps {
                script {
                    def nodeIP = sh(script: "minikube ip", returnStdout: true).trim()
                    echo "App should be available at: http://${nodeIP}:30004"
                }
            }
        }
    }
}

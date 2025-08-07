pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vamshiadep21/mlops-inference-service:latest'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/VamshiAdep/Mlops_DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up dangling images"
            sh "docker image prune -f"
        }
    }
}

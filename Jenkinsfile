pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'sarfraazz72/docker-jenkins-aws-cicd'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv-ci
                    . venv-ci/bin/activate
                    pip install --upgrade pip
                    pip install -r app/requirements.txt
                    pip install pytest
                    pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE}:latest .
                '''
            }
        }

        stage('Docker Test') {
            steps {
                sh '''
                    docker run -d \
                      --name docker-jenkins-test \
                      -p 5001:5000 \
                      ${DOCKER_IMAGE}:latest

                    sleep 5

                    curl -f http://localhost:5001/health

                    docker stop docker-jenkins-test
                    docker rm docker-jenkins-test
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" \
                            --password-stdin
                    '''
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                    docker push ${DOCKER_IMAGE}:latest
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker rm -f docker-jenkins-test 2>/dev/null || true
                docker logout 2>/dev/null || true
                rm -rf venv-ci
            '''
        }

        success {
            echo 'CI/CD pipeline completed successfully!'
            echo 'Docker image pushed to Docker Hub.'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
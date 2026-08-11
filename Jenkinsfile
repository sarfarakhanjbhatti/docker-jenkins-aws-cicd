pipeline {
    agent any

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
                    docker build -t docker-jenkins-aws-cicd:latest .
                '''
            }
        }

        stage('Docker Test') {
            steps {
                sh '''
                    docker run -d \
                      --name docker-jenkins-test \
                      -p 5001:5000 \
                      docker-jenkins-aws-cicd:latest

                    sleep 5

                    curl -f http://localhost:5001/health

                    docker stop docker-jenkins-test
                    docker rm docker-jenkins-test
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker rm -f docker-jenkins-test 2>/dev/null || true
                rm -rf venv-ci
            '''
        }

        success {
            echo 'CI pipeline completed successfully!'
        }

        failure {
            echo 'CI pipeline failed. Check the console output.'
        }
    }
}
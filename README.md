# Docker Jenkins AWS CI/CD 🚀

A production-style CI/CD pipeline that automates testing, Docker image creation, Docker Hub publishing, and deployment of a containerized Flask application to an AWS EC2 instance using Jenkins.

This project demonstrates a complete DevOps workflow using GitHub, Jenkins, Docker, Docker Hub, AWS EC2, SSH authentication, automated testing, health checks, and continuous deployment.

---

## 📌 Project Overview

The application is a simple Flask-based web application that is containerized using Docker.

Jenkins automates the complete CI/CD process:

1. Checkout source code from GitHub
2. Create Python virtual environment
3. Install application dependencies
4. Run automated tests using Pytest
5. Build Docker image
6. Run Docker container for testing
7. Perform application health check
8. Login to Docker Hub securely
9. Push Docker image to Docker Hub
10. Connect to AWS EC2 using SSH
11. Pull the latest Docker image
12. Remove the old application container
13. Start the new application container
14. Perform production health check
15. Complete deployment

---

## 🏗️ CI/CD Architecture

GitHub Repository
        |
        v
     Jenkins
        |
        v
   Checkout Code
        |
        v
   Python Tests
        |
        v
   Docker Build
        |
        v
   Docker Test
        |
        v
  Docker Hub Login
        |
        v
   Docker Push
        |
        v
    SSH to EC2
        |
        v
 Docker Pull Latest Image
        |
        v
 Remove Old Container
        |
        v
 Start New Container
        |
        v
 Application Health Check
        |
        v
   Live Application


---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Git | Version control |
| GitHub | Source code management |
| Jenkins | CI/CD automation |
| Python | Application development |
| Flask | Web application framework |
| Pytest | Automated testing |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| AWS EC2 | Application deployment |
| SSH | Secure EC2 access |
| Linux | Server environment |

---

## 📂 Project Structure

docker-jenkins-aws-cicd/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── Jenkinsfile
├── .dockerignore
├── .gitignore
└── README.md

---

## 🐍 Application

The project contains a Flask application.

The application provides a health-check endpoint:

/health

Expected response:

{"status":"healthy"}

This endpoint is used by Jenkins to verify that the Docker container is running correctly.

---

## 🐳 Docker Configuration

The application is packaged into a Docker image.

Docker image:

sarfraazz72/docker-jenkins-aws-cicd:latest

The Docker image contains:

- Python runtime
- Flask application
- Application dependencies
- Production container configuration

---

## 🔬 Automated Testing

Jenkins creates a Python virtual environment and installs the required dependencies.

Testing workflow:

Python Virtual Environment
        |
        v
Install Dependencies
        |
        v
Install Pytest
        |
        v
Run Tests
        |
        v
Tests Passed

The project tests are located inside:

tests/test_app.py

The pipeline verifies that the application tests pass before creating and deploying the Docker image.

---

## 🐳 Docker Build

Jenkins automatically builds the Docker image using:

docker build -t sarfraazz72/docker-jenkins-aws-cicd:latest .

The Docker image is created only after the application tests pass.

---

## 🧪 Docker Container Test

After building the image, Jenkins starts a temporary container:

docker-jenkins-test

The container runs on:

5001:5000

Jenkins then performs a health check:

http://localhost:5001/health

Expected response:

{"status":"healthy"}

After successful testing, the temporary container is stopped and removed.

---

## 📦 Docker Hub

After the Docker tests pass, Jenkins securely logs into Docker Hub using Jenkins Credentials.

The image is pushed to:

sarfraazz72/docker-jenkins-aws-cicd

Image tag:

latest

Docker workflow:

Docker Build
      |
      v
Docker Test
      |
      v
Docker Hub Login
      |
      v
Docker Push

---

## 🔐 Jenkins Credentials

Sensitive credentials are not stored directly inside the Jenkinsfile.

The project uses Jenkins Credentials Store.

### Docker Hub Credential

Credential ID:

dockerhub-credentials

Used for:

- Docker Hub authentication
- Docker image push

### EC2 SSH Credential

Credential ID:

ec2-ssh-key

Used for:

- Secure SSH authentication
- Jenkins to AWS EC2 deployment

Private SSH keys are not stored inside the GitHub repository.

---

## ☁️ AWS EC2 Deployment

The Docker application is deployed to an AWS EC2 instance.

The EC2 server runs Ubuntu and Docker.

Jenkins connects to the EC2 instance using SSH.

Deployment workflow:

Jenkins
   |
   | SSH
   v
AWS EC2
   |
   v
Docker Pull
   |
   v
Remove Old Container
   |
   v
Start New Container
   |
   v
Health Check
   |
   v
Application Live

---

## 🚀 Automatic EC2 Deployment

Jenkins automatically performs the following operations on EC2:

1. Pull latest Docker image
2. Stop and remove old container
3. Start new container
4. Map EC2 port 80 to container port 5000
5. Wait for application startup
6. Run health check
7. Confirm successful deployment

The production container is named:

docker-jenkins-app

Port mapping:

80:5000

Docker restart policy:

unless-stopped

---

## 🌐 Application Access

During deployment, the application is exposed through:

Port 80

The application can be accessed using:

http://<EC2_PUBLIC_IP>

The exact public IP changes when a new EC2 instance is created because the project uses an auto-assigned public IPv4 address.

---

## ❤️ Health Check

The application provides:

/health

Jenkins uses this endpoint after deployment to verify that the application is running correctly.

Health check command:

curl -f http://localhost/health

Expected response:

{"status":"healthy"}

A successful response confirms that the deployment is working.

---

## 🔄 Jenkins Pipeline Stages

The Jenkins pipeline contains the following stages:

### 1. Checkout

Jenkins checks out the source code from GitHub.

### 2. Test

Creates a Python virtual environment, installs dependencies, and runs Pytest.

### 3. Docker Build

Builds the Docker image.

### 4. Docker Test

Runs the Docker container and performs a health check.

### 5. Docker Hub Login

Authenticates with Docker Hub using Jenkins Credentials.

### 6. Docker Push

Pushes the latest Docker image to Docker Hub.

### 7. Deploy to EC2

Connects to AWS EC2 through SSH and deploys the latest Docker image.

---

## 📋 Jenkins Pipeline Flow

Checkout
   ↓
Test
   ↓
Docker Build
   ↓
Docker Test
   ↓
Docker Hub Login
   ↓
Docker Push
   ↓
Deploy to EC2
   ↓
Health Check
   ↓
SUCCESS

---

## 🔐 Security Practices

This project follows several security practices.

### Jenkins

- Docker Hub credentials stored in Jenkins Credentials
- EC2 SSH private key stored in Jenkins Credentials
- Credentials are not hard-coded in the Jenkinsfile
- SSH authentication uses Jenkins SSH Agent

### GitHub

- Source code stored in GitHub
- `.gitignore` prevents sensitive/local files from being committed
- `.dockerignore` prevents unnecessary files from entering Docker images

### AWS

- SSH access restricted through EC2 Security Group
- HTTP port 80 exposed for application access
- EC2 deployment performed using SSH authentication

---

## 📄 Jenkinsfile

The complete CI/CD process is defined inside:

Jenkinsfile

The Jenkinsfile contains:

- Pipeline configuration
- Environment variables
- Automated testing
- Docker build
- Docker testing
- Docker Hub authentication
- Docker image push
- EC2 deployment
- Health checks
- Post-build cleanup
- Success and failure messages

---

## 🧹 Jenkins Cleanup

After every pipeline execution, Jenkins performs cleanup:

- Removes temporary Docker test container
- Logs out from Docker Hub
- Removes temporary Python virtual environment

This helps keep the Jenkins environment clean.

---

## 🧪 Project Validation

The project was successfully tested through the complete CI/CD workflow:

GitHub Push
      ↓
Jenkins Trigger
      ↓
Python Tests
      ↓
Docker Build
      ↓
Docker Test
      ↓
Docker Hub Push
      ↓
EC2 SSH Connection
      ↓
Docker Image Pull
      ↓
Old Container Removal
      ↓
New Container Deployment
      ↓
Application Health Check
      ↓
Pipeline SUCCESS

The final deployment successfully confirmed:

- Python tests passed
- Docker image built successfully
- Docker health check passed
- Docker image pushed to Docker Hub
- Jenkins successfully connected to EC2
- Docker image pulled on EC2
- Application container started successfully
- Production health check passed

---

## 🧹 AWS Cleanup

After completing the project testing, the AWS EC2 instance was terminated to avoid unnecessary compute charges.

The project environment was cleaned up after successful deployment testing.

Docker Hub and GitHub resources remain available for future deployment.

---

## 🎯 DevOps Skills Demonstrated

This project demonstrates practical knowledge of:

- Linux
- Git
- GitHub
- Jenkins
- Jenkins Pipeline
- CI/CD
- Python
- Flask
- Pytest
- Docker
- Dockerfile
- Docker Networking
- Docker Hub
- Jenkins Credentials
- SSH Authentication
- AWS EC2
- AWS Security Groups
- Application Deployment
- Health Checks
- Automated Deployment
- Infrastructure and Application Automation

---

## 📈 Future Improvements

Possible improvements for this project include:

- Jenkins Webhook integration
- Automatic deployment on every GitHub push
- AWS IAM integration
- AWS OIDC authentication
- Terraform infrastructure provisioning
- Terraform-managed EC2 deployment
- AWS VPC architecture
- Application Load Balancer
- Auto Scaling Group
- Docker image versioning
- Blue-Green Deployment
- Rolling Deployment
- Docker image security scanning
- Trivy integration
- SonarQube integration
- Prometheus monitoring
- Grafana dashboards
- CloudWatch monitoring
- Email notifications
- Slack notifications
- HTTPS using SSL/TLS
- Custom domain name
- Production-grade reverse proxy using Nginx

---

## 🚀 How to Run Locally

Clone the repository:

git clone git@github.com:sarfarakhanjbhatti/docker-jenkins-aws-cicd.git

Navigate into the project:

cd docker-jenkins-aws-cicd

Create a virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

Install dependencies:

pip install -r app/requirements.txt

Install Pytest:

pip install pytest

Run tests:

pytest

Run the Flask application:

python3 app/app.py

---

## 🐳 Run with Docker

Build the image:

docker build -t docker-jenkins-aws-cicd .

Run the container:

docker run -d \
  --name docker-jenkins-app \
  -p 5000:5000 \
  docker-jenkins-aws-cicd

Check the application:

curl http://localhost:5000/health

Expected response:

{"status":"healthy"}

---

## 📦 Docker Hub Image

Docker Hub repository:

sarfraazz72/docker-jenkins-aws-cicd

Image:

sarfraazz72/docker-jenkins-aws-cicd:latest

---

## 👨‍💻 Author

Sarfaraj Khan

DevOps & Cloud Computing

GitHub:

https://github.com/sarfarakhanjbhatti

---

## ⭐ Project Highlights

This project demonstrates a complete real-world CI/CD workflow:

Code
 ↓
GitHub
 ↓
Jenkins
 ↓
Automated Testing
 ↓
Docker Build
 ↓
Docker Testing
 ↓
Docker Hub
 ↓
AWS EC2
 ↓
Docker Deployment
 ↓
Health Check
 ↓
Live Application

Built using Docker, Jenkins, GitHub, Docker Hub, AWS EC2, Python, Flask, and DevOps best practices.
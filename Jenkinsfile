pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MarMarcz/python-calculator.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'apt-get update && apt-get install -y python3-venv || true'
                    } else {
                        error "Installation steps for non-Unix systems are not defined."
                    }
                }
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install --upgrade pip'
            }
        }
        stage('Run tests') {
            steps {
                sh 'venv/bin/python -m unittest discover'
            }
        }
    }
}

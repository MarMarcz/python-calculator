pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MarMarcz/python-calculator.git'
            }
        }
        stage('Install Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'sudo apt-get update'
                        sh 'sudo apt-get install -y python3 python3-venv'
                    } else {
                        error "Python installation steps for non-Unix systems are not defined."
                    }
                }
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install --upgrade pip'
            }
        }
        stage('Run tests') {
            steps {
                sh '. venv/bin/activate && python -m unittest discover'
            }
        }
    }
}

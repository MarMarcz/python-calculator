pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MarMarcz/python-calculator.git'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest test_calculator.py'
            }
        }
    }
}

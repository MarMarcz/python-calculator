pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/MarMarcz/python-calculator.git'
            }
        }
        stage('Install dependencies') {
            steps {
                // Install dependencies if there's a requirements file (optional)
                sh 'pip install -r requirements.txt || true'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
}

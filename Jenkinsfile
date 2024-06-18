pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MarMarcz/python-calculator.git'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
}

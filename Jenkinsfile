pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -l'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python --version || python3 --version'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 main.py || python main.py'
            }
        }
    }
}


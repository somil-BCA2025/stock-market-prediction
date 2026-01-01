pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

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

        stage('Run Python Script') {
            steps {
                sh 'python main.py'
            }
        }
    }
}


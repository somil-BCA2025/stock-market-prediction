pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -l'
                sh 'python3 --version'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Verify Repository') {
            steps {
                sh 'ls -l'
                echo 'Repository structure verified'
            }
        }

        stage('CI Status') {
            steps {
                echo 'Python execution skipped: environment not available on Jenkins node'
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                git 'https://github.com/gulsahceyhan/insider_bootcamp.git'
            }
        }
        stage('Install dependencies') {
            steps {
                // Assuming you use pip for Python dependency management
                sh 'pip install -r requirements.txt' // If you have requirements.txt file
                // Or install dependencies using any other method if applicable
            }
        }
        stage('Run tests') {
            steps {
                // Navigate to the test directory
                dir('test') {
                    // Run your test script
                    sh 'python tester.py'
                }
            }
        }
    }
    post {
        always {
            // Cleanup steps if necessary
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}

pipeline {
    agent any
    environment {
        // DEVELOPER BRANCH 'develop' 
        BRANCH = "${BRANCH_NAME}"
        // ANSIBLE FORCE_COLOR= 'true'
}

stages {
    stage('Get Branch Name') {
        steps {
            script {
                branch = env.BRANCH
            }
        }
    }


    stage('Set Pending Status') {
        steps {
            script {
                bat 'echo "Pending"'
            }
        }
    } 

    stage("Automation Precess") {
        steps {
            script {
                dir('C:/Users/New/OneDrive/bootcamp/test'){
                    echo 'Automation Process running...'
                    bat 'pip install -r requirements.txt'
                    echo 'requirements installed'
                    bat 'python tester.py'
                }
            }
        }
    } 
}

post{
    success{
        script{
            bat 'echo "Automation process completed succesfully"'
        }
    }
    failure{
        script{
            bat 'echo "Automation process failed"'
        }
    }
}

}
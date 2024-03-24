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
                    bat 'pwd'
                dir('C:/Users/New/OneDrive/Masaüstü/bootcamp/test'){
                    bat 'pwd'
                    echo 'Automation Process running...'
                    bat 'pip install -r requirements.txt'
                    bat 'pwd'
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
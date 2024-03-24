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
                sh 'echo "Pending"'
            }
        }
    } 

    stage("Automation Precess") {
        steps {
            script {
                dir('C:/Users/New/OneDrive/Masaüstü/bootcamp/test'){
                    echo 'Automation Process running...'
                    sh 'pip install -r requirements.txt'
                    sh 'pwd'

                    // sh command
                    // sleep(time:30, unit 'SECONDS')
                }
            }
        }
    } 
}

post{
    succes{
        script{
            sh 'echo "Automation process completed succesfully"'
        }
    }
    failre{
        script{
            sh 'echo "Automation process failed"'
        }
    }
}

}
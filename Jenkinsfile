pipeline {
    agent any
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
        AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
    }
    stages {
        stage('build') {
            steps {
               echo "Database engine is ${DB_ENGINE}"
               echo "DISABLE_AUTH is ${DISABLE_AUTH}"
               echo "AWS_ACCESS_KEY_ID is ${AWS_ACCESS_KEY_ID}"
               echo "AWS_SECRET_ACCESS_KEY is ${AWS_SECRET_ACCESS_KEY}"
               bat 'py -3 --version'
            }
        }
        stage('test') {
            steps {
                bat 'py -3 py-tests.py'
            }
        }
        stage('deploy') {
            steps {
                timeout(time:3,unit:'MINUTES'){
                    retry(3) {
                        bat './fake-deploy.py'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}

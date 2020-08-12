pipeline {
    agent any
    stages {
        stage('build') {
            steps {
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

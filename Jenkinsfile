node {
    stage('Build') {
        bat 'set'
    }
    
    stage('Deloy') {
        timeout(time:3, unit:'MINUTES'){
            retry(3) {
                bat 'flakey-deploy.sh'   
            }
        }
    }
}

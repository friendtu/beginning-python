node {
    withEnv(['DISABLE_AUTH=True','DB_ENGINE=sqlite']){
        try {
            stage('Build') {
                echo "DISABLE_AUTH: ${DISABLE_AUTH}"
                echo "DB_ENGINE: ${DB_ENGINE}"
            }
            echo 'This will run only if successful'
        } catch (e) {
            echo 'This will run on if failed'
            throw e
        } finally {
        if( currentBuild.result=='SUCCESS')
                echo "run for success"
        if (currentBuild.result=='UNSTABLE') 
                echo "run for unstable"
            if(currentBuild.result=='FAILURE')
                echo "run for failure"
        }
    }
}

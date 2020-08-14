node {
    try {
        stage('Build') {
            bat 'set'
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

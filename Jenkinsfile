node {
    try {
        stage('Build') {
            bat 'echo "Fail";exit -1'
        }
        echo 'This will run only if successful'
    } catch (e) {
        echo 'This will run on if failed'
    }
}

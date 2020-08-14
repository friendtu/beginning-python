node {
    try {
        stage('Build') {
            bat 'set;exit -1'
        }
        echo "This will run only if successful'
    } catch (e) {
        echo 'This will run on if failed'
    }
}

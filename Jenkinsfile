node {
    try {
        stage('Build') {
            bat 'fake.bat'
        }
        echo 'This will run only if successful'
    } catch (e) {
        echo 'This will run on if failed'
    }
}

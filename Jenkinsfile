properties([
    parameters([
        booleanParam(defaultValue: true, description: 'if it will send mail', name: 'ToSendmail')
        ])
    ])

node('inventorqabuild') {
    withEnv(['DISABLE_AUTH=True','DB_ENGINE=sqlite']){
        try {
            JIRA_ACCOUNT=credentials("jira_account")
            stage('Build') {
                echo "ToSendmail: ${params.ToSendmail}"
                echo "DISABLE_AUTH: ${DISABLE_AUTH}"
                echo "DB_ENGINE: ${DB_ENGINE}"
                echo "JIRA_ACCOUNT: ${JIRA_ACCOUNT}"
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

    stage('Sanity check') {
        input "Does the staging environment look ok?"
        echo "do sanify checking..."
    }
}

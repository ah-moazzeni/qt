pipeline {
    agent any
    environment {
        PROJECT_NAME = 'hello_app'
        DIST_DIR = 'dist'
    }
    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install pyinstaller PyQt5
                '''
            }
        }
        stage('Build Executable') {
            steps {
                sh '''
                source venv/bin/activate
                pyinstaller --onefile ${PROJECT_NAME}.py
                '''
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: "${DIST_DIR}/*", allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            cleanWs() // Clean workspace after build
        }
    }
}

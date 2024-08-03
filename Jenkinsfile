pipeline {
    agent any
    environment {
        PROJECT_NAME = 'hello_app'
        DIST_DIR = 'dist'
    }
    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install pyinstaller PyQt5'
            }
        }
        stage('Build Executable') {
            steps {
                sh "pyinstaller --onefile main.py"
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

pipeline {
    agent any
    environment {
        PROJECT_NAME = 'hello_app'
        DIST_DIR = 'dist'
        VENV_DIR = 'venv'
    }
    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                # Use Bash shell explicitly
                bash -c "
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
//                 pip install --upgrade pip
                pip install pyinstaller PyQt5
                "
                '''
            }
        }
        stage('Build Executable') {
            steps {
                sh '''
                # Use Bash shell explicitly
                bash -c "
                source ${VENV_DIR}/bin/activate
                pyinstaller --onefile main.py
                "
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

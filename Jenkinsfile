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
                #!/bin/bash
                # Create a virtual environment
                python3 -m venv ${VENV_DIR}

                # Activate the virtual environment
                source ${VENV_DIR}/bin/activate

                # Upgrade pip to ensure compatibility
                pip install --upgrade pip

                # Install necessary packages within the virtual environment
                pip install pyinstaller PyQt5
                '''
            }
        }
        stage('Build Executable') {
            steps {
                sh '''
                #!/bin/bash
                # Activate the virtual environment
                source ${VENV_DIR}/bin/activate

                # Use pyinstaller to create a standalone executable
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

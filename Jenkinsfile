pipeline {
    agent any
    environment {
        PROJECT_NAME = 'hello_app'
        DIST_DIR = 'dist'
        VENV_DIR = 'venv'
//         LD_LIBRARY_PATH = '/usr/local/glibc-2.36/lib' // Adjust this path if needed
    }
    stages {
    stage('Install Dependencies') {
            steps {
                sh '''
                # Ensure necessary libraries are installed
                 apt-get update
                apt-get install -y libglib2.0-0 libxkbcommon-x11-0 libxcb1 libxcb-render0 libxcb-shape0 libxcb-xfixes0
                '''
            }
        }
    stage('Setup Python Environment') {
        steps {

                sh '''
                # Set LD_LIBRARY_PATH and use Bash shell explicitly
                /bin/bash -c "
                export LD_LIBRARY_PATH=/usr/local/glibc-2.36/lib:$LD_LIBRARY_PATH
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
//                 pip install --upgrade pip
                pip install pyinstaller
                pip install PyQt5
                pip install PyQt5-sip
                "
                '''
            }
        }
        stage('Build Executable') {
            steps {
                sh '''
                # Set LD_LIBRARY_PATH and use Bash shell explicitly
                /bin/bash -c "
                export LD_LIBRARY_PATH=/usr/local/glibc-2.36/lib:$LD_LIBRARY_PATH
                source ${VENV_DIR}/bin/activate
                pyinstaller --onefile --hidden-import=PyQt5.QtCore --hidden-import=PyQt5 --hidden-import=PyQt5.sip --hidden-import=PyQt5.QtGui main.py
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

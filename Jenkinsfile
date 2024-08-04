pipeline {
    agent any
    environment {
        PROJECT_NAME = 'hello_app'
        DIST_DIR = 'dist'
        VENV_DIR = 'venv'
          GLIBC_DIR = '/opt/glibc-2.36'
    }
    stages {
 stage('Setup glibc') {
            steps {
                sh '''
                #!/bin/bash
                if [ ! -d "${GLIBC_DIR}" ]; then
                    wget http://ftp.gnu.org/gnu/libc/glibc-2.36.tar.gz
                    tar -xzvf glibc-2.36.tar.gz
                    cd glibc-2.36
                    mkdir build
                    cd build
                    ../configure --prefix=${GLIBC_DIR}
                    make -j4
                    sudo make install
                fi
                export LD_LIBRARY_PATH=${GLIBC_DIR}/lib:$LD_LIBRARY_PATH
                '''
            }
        }
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

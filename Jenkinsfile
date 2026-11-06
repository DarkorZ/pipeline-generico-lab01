
pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout()
    }
    
    triggers {
        pollSCM('H/5 * * * *')
    }
    
    parameters {
        booleanParam(
            name: 'FORZAR_FALLO',
            defaultValue: false,
            description: 'Simular fallo del pipeline'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Preparar entorno') {
            steps {
                sh 'uv venv --python 3.12 .venv'
                sh 'uv pip install --python .venv/bin/python -r requirements-ci.txt'
            }
        }

        stage('Pruebas') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Calidad') {
            steps {
                sh '.venv/bin/python -m ruff check .'
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    if (params.FORZAR_FALLO) {
                        error('Fallo controlado del laboratorio')
                    }
                }
            }
        }

        stage('Build') {
            steps {
                sh '.venv/bin/python -m build'

                archiveArtifacts(
                    artifacts: 'dist/*',
                    fingerprint: true
                )
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }

        failure {
            echo 'El pipeline ha fallado'
        }
    }
}

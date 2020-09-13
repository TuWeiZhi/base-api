pipeline {
  agent {
    node {
      label '39-107-233-152'
    }

  }
  stages {
    stage('shell') {
      steps {
        sh '''whoami
echo $dt'''
      }
    }

  }
  environment {
    dt = '`date +"%Y-%m-%d" `'
  }
}
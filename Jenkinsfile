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
dt=`date +"%Y-%m-%d"`
echo $dt'''
      }
    }

  }
}
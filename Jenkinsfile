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
dt=`date +"%Y-%m-%d"`'''
      }
    }

    stage('date') {
      steps {
        sh 'docker run -tid --name=back-fish-`date +"%Y-%m-%d"` tuweizhi/basic-ubuntu18:20200626'
      }
    }

  }
}
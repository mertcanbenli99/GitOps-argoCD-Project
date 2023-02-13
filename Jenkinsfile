pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME="mert5432100"
        APP_NAME="gitops-argo-app"
        IMAGE_TAG="${BUILD_NUMBER}"
        IMAGE_NAME= "${DOCKERHUB_USERNAME}" + "/" + "${APP_NAME}"
        REGISTRY_CREDS= "dockerhub"
    }

    stages{

      stage("cleanup workspace") {

        steps{
            script{
                cleanWs()
            }
        }
      }
      stage("Checkout SCM") {
        steps {
          script {
             git credentialsId: "github",
             url: "https://github.com/mertcanbenli99/GitOps-argoCD-Project.git",
             branch: "main"
          }

        }
      }

      
    }
}


// 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 github
//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
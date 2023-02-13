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
      stage("Docker Image Build") {
        steps {
          script {
            docker_image = docker.build "${IMAGE_NAME}"
          }
        }
      }
      stage("Push Docker Image to Hub") {
        steps {
          script {
            docker.withRegistry('', REGISTRY_CREDS) {
              docker_image.push("${BUILD_NUMBER}")
              docker_image.push("latest")
            }
          }
        }
      }
      stage("Delete Docker Images") {
        steps {
          script {
            sh "docker image remove ${IMAGE_NAME}:${IMAGE_TAG}"
            sh "docker image remove ${IMAGE_NAME}:latest"
          }
        }
      }

      stage("Update kubernetes deployment file") {
        steps {
          script {
            sh """
             cat deployment.yml
             sed -i '/s${APP_NAME}.*/${APPNAME}:${IMAGE_TAG}/G' deployment.yml
             cat deployment.yml
            """
          }
        }
      }

      
    }
}

@Library('my-shared-library') _

pipeline{

    agent any
    //agent { label 'Demo' }

    parameters{

        choice(name: 'action', choices: 'create\ndelete', description: 'Choose create/Destroy')
        string(name: 'ImageName', description: "name of the docker build", defaultValue: 'javapp')
        string(name: 'ImageTag', description: "tag of the docker build", defaultValue: 'v1')
        string(name: 'DockerHubUser', description: "name of the Application", defaultValue: 'nemidevops')
        string(name: 'ARTIFACTORY_USERNAME', description: 'Artifactory Username', defaultValue: 'admin')
        password(name: 'ARTIFACTORY_PASSWORD', description: 'Artifactory Password', defaultValue: 'password')
        string(name: 'REPOSITORY_NAME', description: 'Artifactory Repository Name', defaultValue: 'java-app')
        string(name: 'ARTIFACT_FILE', description: 'Path to Artifact File', defaultValue: '/var/lib/jenkins/workspace/clss4-assignment/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar')
        string(name: 'ARTIFACTORY_URL', description: 'Artifactory URL', defaultValue: 'http://139.59.68.101:8081/artifactory/java-app/')
    }

    stages{
         
        stage('Git Checkout'){
                    when { expression {  params.action == 'create' } }
            steps{
            gitCheckout(
                branch: "main",
                url: "https://github.com/Nemidevops/javapp-3.0.git"
            )
            }
        }
         stage('Unit Test maven'){
         
         when { expression {  params.action == 'create' } }

            steps{
               script{
                   
                   mvnTest()
               }
            }
        }
         stage('Integration Test maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnIntegrationTest()
               }
            }
        }
        stage('Static code analysis: Sonarqube'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   def SonarQubecredentialsId = 'sonarqube-api'
                   statiCodeAnalysis(SonarQubecredentialsId)
               }
            }
       }
       stage('Quality Gate Status Check : Sonarqube'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   def SonarQubecredentialsId = 'sonarqube-api'
                   QualityGateStatus(SonarQubecredentialsId)
               }
            }
       }
        stage('Maven Build : maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnBuild()
               }
            }
        }
        stage('Push to JFrog Artifactory') {
            steps {
                script {
                    def command = "curl -u ${env.ARTIFACTORY_USERNAME}:${env.ARTIFACTORY_PASSWORD} -T ${env.ARTIFACT_FILE} ${env.ARTIFACTORY_URL}"
                    sh(command)
                }
            }
        }   
        stage('Docker Image Build'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerBuild("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
         stage('Docker Image Scan: trivy '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageScan("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
        stage('Docker Image Push : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImagePush("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }   
        stage('Docker Image Cleanup : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageCleanup("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }      
    }
}

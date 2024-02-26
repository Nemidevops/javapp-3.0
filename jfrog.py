#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload() :
    # define the url file path, and authentication credentials and change ur IP Address
    url = 'http://157.245.106.219:8081/artifactory/java-app/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/var/lib/jenkins/workspace/clss4-assignment/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'password'

    #send the PUT request with authentication and file upload
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
    #check the response.status code
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print("PUT request failed with status code (response.status_code)")
        print("response content:")
        print(response.text)
def main() :
    #mvnBuild()
    jfrogUpload()

if __name__ == "__main__":
    main()

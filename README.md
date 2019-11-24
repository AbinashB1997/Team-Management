#### This project will enhance the concepts of docker and kubernetes. And this is a good project to start with. 

### Prerequisite: 
    Host machine requirements:
      1. Python
         1.1. Flask
         1.2. Pymongo
      2. Docker
         installation: https://docs.docker.com/install/linux/docker-ce/ubuntu/
      3. Kubernetes
         3.1. Kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl/
         3.2. Minikube: https://kubernetes.io/docs/tasks/tools/install-minikube/
      4. MongoDB for host-machine
         Installation: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
      5. Editor 
         (I have used vs-code, and I will recommend it to be used. You can use any of the available editors, instead)
         
### Let's get started after all installation
    Please make sure the mongodb is up and running in the machine by firing a command 'mongo' in the CLI. 
    If it routes you to the mongodb interfac, you will see a ('>') sign there. If yes, then enter 'exit' 
    and come back to CLI. Else, try to find the mongodb is up or not.
    
### Step1: 
    - Download the complete folder
    - UnZip it
### Step2:
    - RUN => minikube start
    - RUN => minikube service myapp-frontend-service
### Step3:
      Enjoy using the app.

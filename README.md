# Cloud Computing Hands on using Google Cloud
Repository containing the instructions and scripts for getting started with Google cloud


## Set up your GCP Acccount and Launch an instance

1. Use the code and sign up for a GCP account
2. Log in to the console
3. From the side menu panel, select Compute Engine and click on "Enable API"
4. Launch an instance from Compute engine screen with basic 1Gb RAM, 10 GB persistence,  Ubuntu 64-bit version
5. Click on the instance and select the edit option. Go to the "ssh keys" section
7. Go back to your local machine. If you are using a mac or Linux machine, go to the terminal and type: ssh-keygen -t rsa.
8. Paste your public key (id_rsa.pub - the default key) in the metadata section (to copy the public key just do cat id_rsa.pub and copy the contents)
9. For mac users, it will be created in cd /Users/<username>/.ssh by default 
10. Find the external IP of the instance from the home page
11. Log in to the instance using ssh -i <private_key> username@instance_ip (example: ssh -i id_rsa karthik@38.12.116.122)
12. You are now inside your GCP instance. 
    
### For Windows Users
1. After step 5 above, download the program "Putty" from https://www.puttygen.com/download-putty#Download_PuTTY_073_for_Windows
2. Use the program puttygen to generate the public and private keys. Follow the instructions in https://medium.com/@narayanan_ramakrishnan/connecting-to-a-google-cloud-virtual-machine-with-ssh-using-putty-7b6f0c0465cb
    
    
## Deploying a microservice
1. Copy the Login service folder to your instance using command: scp -i key.pem -r /path-to-your-code/ username@ipadress:/home/username/foldername/
2. Check if Python3 is installed in the instance by typing: python3. By default Python will be installed in your instance

### Set up the Python Environment

1. sudo apt-get update
2. sudo apt-get -y install python3-pip
3. pip3 install tornado
4. pip3 install requests
 

3. Go inside the folder Login Service: cd Login_Service/app
4. Run the microservice: python3 app.py
5. You will be able to see a message "Starting Tornado Web Server for Login Service on 8895" which shows that the service is running

    
### Testing your microservice
1. Configure the firewall rules to enable the port.
2. From the menu of the instance -> select network details -> Create firewall rule
3. Add the port number(s) to which the access has to be provided.
4. Add the tag by editing the instance (Network-tags)
5. Make a rest call to your service using the JSON. To do this, you can either make use of RESTED client (plugin for Google Chrome - https://chrome.google.com/webstore/detail/rested/eelcnbccaccipfolokglfhhmapdchbfg) or using POSTMAN - https://www.postman.com/downloads/
    
  ```shell
    {
     "username" : "sample",
     "password" : "sample123"
    }
   ```
    
6. If everything goes correctly you will get a JSON with successfull response:
    
  ```shell
    {
  "status": "success",
  "login": "success"
    }
  ```
    

Disclaimer: Better way is to provide access via a proxy. Please find the instructions below

## Install Apache web server
    
1. sudo apt-get update
2. sudo apt-get install apache2
3. sudo apt-get install vim (For easy editing)


## Configure Apache for Proxy
1. sudo a2enmod proxy
2. sudo a2enmod proxy_http
3. sudo a2enmod proxy_balancer
4. sudo a2enmod lbmethod_byrequests
5. sudo systemctl restart apache2
6. cd /etc/apache2/sites-available
7. sudo vim 000-default.conf 
8. Inside the <Virtualhost:*80> add the following  (press insert button to edit, for mac users, press "i")

    ProxyPreserveHost On

    ProxyPass /auth http://localhost:8895/login

    (Press "esc :wq" to save and exit vim)

 9. Test your service by making a REST request to the URL: http://<gcp instance ip>/auth

You have successfully deployed a web service on your instance !!
    
## Containerizing your microservice
    
### Installing Docker
    
For Linux/Mac users:
    
1. sudo apt-get update
2. sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4. echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5. sudo apt-get update
6. sudo apt-get install docker-ce docker-ce-cli containerd.io
7. Test the installation: sudo docker run hello-world
    
### Building the Container

1. cd in to the Login_Service directory
2. There will be a file named "Dockerfile". Verify if the structure is correct

```shell
    sudo docker build -t login_service .
    sudo docker run -it --name login_container -p 8895:8895 login_service
```
3. Make calls using REST to test the login service
    

## Dockerhub
    
1. docker pull karthikv1392/login_service:latest
2. docker run --rm -p 8895:8895 docker/versekarthikv1392/login_service:tagname
 
 



# Kafka Commands

Source : https://kafka.apache.org/quickstart



Start Zookeeper

bin/zookeeper-server-start.sh config/zookeeper.properties



Start Kafka Server

bin/kafka-server-start.sh config/server.properties


Create topic

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test


Send Messages

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test



Start a consumer

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning


List topics

bin/kafka-topics.sh --list --bootstrap-server localhost:9092



## Exercise

1. Deploy a hello world app in the app engine https://cloud.google.com/appengine/docs/standard/python/quickstart
2. Install Jupyter notebook in your instance and access it from your local machine

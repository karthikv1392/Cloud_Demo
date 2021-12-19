# Cloud_Demo
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
7. sudo vim 000-default-sites.conf
8. Inside the <Virtualhost:*80> add the following  (press insert button to edit, for mac users, press "i")

    ProxyPreserveHost On

    ProxyPass /auth http://localhost:8895/login

    (Press "esc :wq" to save and exit vim)

### Enable Google Vision API

1. From the navigation menu in the Google Cloud Services, select "API's and Services"
2. Above will take you inside the dashboard view of API's and servies, Press "Enable APIs and Services" button (with + sign)
3. Search for "Cloud Vision API" in the search bar and press enter
4. Click on "Cloud Vision API" and click on the "Enable" button
5. Go back to the Google Cloud main console
6. Select "API's and Services" from the navigation menu on the left
7. Click on "Credentials" from the left pane
8. Press "Create Credentials" -> "API key"
9. A key will be created, Copy the key and paste it in a text in your local machine "api_key.txt"

### Starting the Service

1. Go to the directory where the code has been copied
2. Open the settings.conf using command vim settings.conf
3. Add the copied API key in the api_key field of settings.conf
4. Save and exit settings.conf (esc :wq)
5. Run the services using the command "Python Vision_Service.py"
6. You should be able to see "Starting service on Port 8065"

### Making Request to the WebService

1. Go back to your local machine and open "upload_post_server.html" from the clonned Git repository
2. Edit the line 8 of the html using text editor (This line <form enctype="multipart/form-data" action="http://localhost:8065/analyze" method="post">)
3. Replace the url in line 8 with "http://yourinstanceip/getImageDetails"
4. Open the html in a browser, click on the upload button and select any image file
5. Click submit and check the response
    

You have successfully deployed a web service on your instance !!
 
## Exercise

1. Deploy a hello world app in the app engine https://cloud.google.com/appengine/docs/standard/python/quickstart
2. Install Jupyter notebook in your instance and access it from your local machine


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





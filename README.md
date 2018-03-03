# awsAPI
AWS Utilities 

configure aws environment:  
$ pip3 install awscli   
$ aws configure  
AWS Access Key ID [None]: access_key  
AWS Secret Access Key [None]: secret_access_key  
Default region name [None]: us-east-1  
Default output format [None]: json  

Following files will be created   
$ cat ~/.aws/credentials  
$ cat ~/.aws/config  

Create a new python folder,virtual env, install boto3
$ mkdir awsSNSpublish
$ python3 -m venv vawssns
$ source vawssnstest/bin/activate
$ pip3 install boto3

If you are inside the firewall, add proxy to config file
$ cat ~/.aws/config
[default]
proxy=http://myproxy


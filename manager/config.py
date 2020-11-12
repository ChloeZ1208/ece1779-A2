subnet_id = 'subnet-db57afea'
ami_id = 'ami-0bf618774e7879c6a'

#instance  user1
image_id = ''
Iam_profile = { 'Name': 'ece1779a2'}
SecurityGroup_id = ['sg-05428fb146ee292de']
key_name = 'a2worker0'

# define userdata to run user-app at instance launch
user_data = "#!/bin/bash\n screen\n /home/ubuntu/Desktop/ece1779a1/start.sh"

#elb target group ARN
targetgroup = 'targetgroup/ece1779a2user/da2f671e55d83fc0'
targetgroupARN = 'arn:aws:elasticloadbalancing:us-east-1:327200236258:targetgroup/ece1779a2user/da2f671e55d83fc0'
#elb
loadbalancer = 'app/ece1779a2/5f33ad35c054e2bb'
loadbalancerARN = 'arn:aws:elasticloadbalancing:us-east-1:327200236258:loadbalancer/app/ece1779a2/5f33ad35c054e2bb'
loadbalancerDNS = 'ece1779a2-1322249347.us-east-1.elb.amazonaws.com'

# RDS - database
db_config = {'user': '',
             'password': '',
             'host': '',
             'database': ''}

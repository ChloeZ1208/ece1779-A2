subnet_id = 'subnet-db57afea'
ami_id = 'ami-0bf618774e7879c6a'

#instance  user1
image_id = ''
Iam_profile={
    'Name': 'ece1779a2'
}
SecurityGroup_id = ['sg-05428fb146ee292de']
key_name = 'a2worker0'
# define userdata to run user-app at instance launch
user_data = "#!/bin/bash\n./home/ubuntu/Desktop/start.sh \n"

#elb target group ARN
ARN = 'arn:aws:elasticloadbalancing:us-east-1:327200236258:targetgroup/ece1779a2user/da2f671e55d83fc0'

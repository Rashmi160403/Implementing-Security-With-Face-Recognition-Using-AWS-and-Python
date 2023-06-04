#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import boto3

def lambda_handler(event, context):
  
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    
    cmd = { "commands": [ "usermod -L rashmi" ] }
    
    ssm_client.send_command(DocumentName="AWS-RunShellScript", InstanceIds=["i-01f98a6e2f16e481a"], Parameters=cmd )
    
    return {
        'statusCode': 200,
        'body': json.dumps('User Locked!')
    }


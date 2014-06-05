__author__ = 'himel'

import boto
import os
from boto.ec2 import connect_to_region

access_key = "xyz"
secret_key = "zxc"

username = 'himel'
ami_id = 'ami-001100'
instance_type = 'm1.large'

name = 'code-test-01'
env = 'dev'
role = 'code-test-instance'

availability_zone = 'us-east-1B'
ssh_key_name = 'us-east'
ssh_keyfile_path = os.path.join(os.path.dirname(__file__), 'us-east.pem')


def create_instance():
    conn = connect_to_region(availability_zone, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    res = conn.run_instances(ami_id, key_name=ssh_key_name, instance_type=instance_type)
    instance = res.instances[0]

    conn.create_tags([instance.id], {'Name': name, 'Env': env, 'Role': role})


create_instance()

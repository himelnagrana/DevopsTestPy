__author__ = 'himel'


import boto
import collections

access_key = "xyz"
secret_key = "zxc"

#  defining structure for SecurityGroupsRule
SecurityGroupRule = collections.namedtuple("SecurityGroupRurle", ["ip_protocol", "from_port", "to_port", "cidr_ip", "src_group_name"])

#  assigning rules to the security group
rules = [
    SecurityGroupRule("tcp", "22", "22", "222.111.66.77/32", 'code-test-access'),
    SecurityGroupRule("tcp", "80", "80", "0.0.0.0/0", 'code-test-access'),
]

#  attaching rules with group name
security_groups = [("code-test-access", rules)]


def update_group_with_rules(conn, group, expected_rules):
    for rule in expected_rules:
        source_group = conn.get_all_security_groups([rule.src_group_name])[0]
        group.authorize(ip_protocol=rule.ip_protocol, from_port=rule.from_port, to_port=rule.to_port, cidr_ip=rule.cidr_ip, src_group=source_group)


def check_if_group_exists(conn, group_name):
    groups = [g for g in conn.get_all_security_groups() if g.name == group_name]
    group = groups[0] if groups else None

    if not group:
        return False

    return group


def create_security_group(conn, group_name):
    group = conn.create_security_group(group_name, "A group for %s"%(group_name,))
    return group


def create_security_groups():
    conn = boto.connect_ec2(aws_access_key_id=access_key, aws_secret_access_key=secret_key)     # connecting with credentials

    for group_name, group_rules in security_groups:
        check = check_if_group_exists(conn, group_name)     #  checking if the group we are trying to insert already exists

        if not check:
            #  no the group does not exists - so create a new one and update the group rules
            group = create_security_group(conn, group_name)
            update_group_with_rules(conn, group, group_rules)
        else:
            print "group already exists! updating rules"
            update_group_with_rules(conn, check, group_rules)
            exit()


#  calling to the function
create_security_groups()

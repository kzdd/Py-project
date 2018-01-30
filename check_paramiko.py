import os
import paramiko
import sys


hostname = "73.170.151.236"
password = "oranges123"
command = "mv /tmp/kai.txt /root"

username = "root"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print stdout.read(),

finally:
    client.close()
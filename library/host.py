import paramiko
import socket

class Host:

    def __init__(self, hostname, **kwargs):
        self.hostname = hostname
        self.os = 'Linux'
        self.user = 'root'
        self.password = 'oranges123'
        self.ssh_hdl = None

        self.connect()

        self.ip_addr = socket.gethostbyname(hostname)

    def connect(self, **kwargs):
        self.ssh_hdl = paramiko.SSHClient()
        self.ssh_hdl.load_system_host_keys()
        self.ssh_hdl.set_missing_host_key_policy(paramiko.WarningPolicy)

        retries = 50

        #TODO add retry logic if first connection fails
        try:
            self.ssh_hdl.connect(self.hostname, username=self.user, password=self.password)
        except Exception as e:
            raise e

    def execute(self, cmd, **kwargs):
        print(cmd)
        stdin, stdout, stderr = self.ssh_hdl.exec_command(cmd)


    def get_stdout(self):
        pass


    def get_stderr(self):
        pass



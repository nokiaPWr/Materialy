import os
import paramiko
ssh = paramiko.SSHClient()
privkey = paramiko.RSAKey.from_private_key_file(os.path.expanduser("~/.ssh/id_rsa"))
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("127.0.0.1", username='ogrodnic', pkey=privkey)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls .')



print("output", ssh_stdout.read())
error = ssh_stderr.read()
print("err", error, len(error))

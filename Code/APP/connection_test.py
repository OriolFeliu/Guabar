import os
import paramiko

class connectionRasp():

	rasp_ip = '192.168.1.131'
	username = 'ivan'
	passwd = '4757'

	def comandSSH(self,cmd):
		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(self.ip,22,self.user,self.passwd,timeout=5)
			stdin,stdout,stderr = ssh.exec_command(cmd)
			print("OUT: ", stdout.readlines())
			ssh.close()
		except:
			print("problems")


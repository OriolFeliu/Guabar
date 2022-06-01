import os
import paramiko

class connectionRasp():

	rasp_ip = '192.168.1.131'
	username = 'pi'
	passwd = 'raspi'

	def comandSSH(self,cmd):
		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(self.rasp_ip,22,self.username,self.passwd,timeout=5)
			stdin,stdout,stderr = ssh.exec_command(cmd)
			print("OUT: ", stdout.readlines())
			ssh.close()
		except:
			print("problems")


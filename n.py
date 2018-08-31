import socket
import time
import subprocess
import os

def GetHostName():
	print (socket.gethostname())

def GetDate():
	print (time.strftime("%d/%m/%Y"))

def GetIP():
	Ip = socket.gethostbyname(socket.getfqdn())
	IpArray = Ip.split ('.')
	i = 1
	for element in IpArray:
		print (i, '-', element)
		i+=1

def GetPs():
	proc_list = subprocess.Popen('tasklist', shell=False, stdout=subprocess.PIPE)
	tasklist = os.popen("tasklist").read()
	print (tasklist)

	
x = 1
while x == 1:	
	print ("Введите команду")
	command = input()
	if command == 'gethostname':
		GetHostName()
	elif command == 'getdate':
		GetDate()
	elif command == 'exit':
		x = 2
	elif command == 'getip':
		GetIP1()
	elif command == 'exit':
		x = 2
	elif command == 'getps':
		GetPs()
	else: print ("Неверная команда!")

print ("До скорой встречи!")



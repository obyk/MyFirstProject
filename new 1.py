import socket
import time
import subprocess

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
	print(*[line.split() for line in subprocess.check_output("tasklist").splitlines()])
	
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



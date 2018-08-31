import socket
import time

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

def GetIP1():
	Ip = socket.gethostbyname(socket.getfqdn())
	IpArray = Ip.split ('.')
	i = len(IpArray)-1
	n = 1
	while i>=0:
		print (n, '-', IpArray[i])
		n+=1
		i-=1
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
	else: print ("Неверная команда!")

print ("До скорой встречи!")


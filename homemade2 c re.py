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
	Ps = subprocess.Popen('tasklist', shell=True, stdout=subprocess.PIPE)
	tasklist = os.popen('tasklist').read()
	b = bytes(tasklist,"cp1251")
	s = str(b,"cp866")
	print(s)
	y = 2
	while y == 2:
		print("Введите фильтр")
		word = input()
		fil = s[s['ids'].str.contains(word, na = False)]
			print(fil)
		if word  == 'exit':
			y = 2
			
		
		
		

x = 1
while x == 1:	
	print ("Введите команду")
	command = input()
	if command == 'gethostname':
		GetHostName()
	elif command == 'getdate':
		GetDate()
	elif command == 'getip':
		GetIP1()
	elif command == 'exit':
		x = 2
	elif command == 'getps':
		GetPs()
	else: print ("Неверная команда!")

print ("До скорой встречи!")
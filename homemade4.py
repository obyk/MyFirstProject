import socket
import time
import subprocess
import csv

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
	Ps = subprocess.Popen('tasklist.exe /fo csv', stdout=subprocess.PIPE, universal_newlines=True)
	tasks = subprocess.check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
	reader = csv.reader(tasks)
	for row in reader:
		print(" ".join(row))


x = 1
while x == 1:
	print ("Введите команду")
	command = input()
	if command == 'gethostname':
		GetHostName()
	elif command == 'getdate':
		GetDate()
	elif command == 'getip':
		GetIP()
	elif command == 'exit':
		x = 2
	elif command == 'getps':
		GetPs()
	else: print ("Неверная команда!")

print ("До скорой встречи!")

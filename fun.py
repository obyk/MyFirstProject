import command
import socket
import time

def GetHostName():
	print (socket.gethostname())

def GetDate():
	print (time.strftime("%d/%m/%Y"))
	
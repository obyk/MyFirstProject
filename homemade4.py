## -*- coding: utf-8 -*-
import socket
import time
import subprocess
import csv
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
  tasks = subprocess.check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
  reader = csv.reader(tasks)
  print(reader)
  for row in reader:
    print(" ".join(row))

def PsFilter():
  print ("Введите имя процесса")
  exeName = input ()
  tasks = subprocess.check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
  reader = csv.reader(tasks)
  for row in reader:
          process = " ".join(row)
          if exeName in process: print (process)


x = 1
while x == 1:
  t = ("1.Имя компьютера;2.Дата;3.IP адрес;4.Список процессов;5.Поиск процесса;6.Выход;Для продолжения введите код команды")
  li = str(t).split(';')
  for row in li:
    print("".join(row))
  
  command = input()
  if command == '1':
      GetHostName()
  elif command == '2':
      GetDate()
  elif command == '3':
      GetIP()
  elif command == '6':
      x = 2
  elif command == '4':
      GetPs()
  elif command == '5':
      PsFilter()
  else: print ("Неверная команда!")

print ("До скорой встречи!")

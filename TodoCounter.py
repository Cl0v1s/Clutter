#coding: utf-8

import sys
import re
from os import listdir
import os
from os.path import isfile, join

matchs = [];
files = [];

def listFiles(dir):
	for f in listdir(dir):
		if isfile(join(dir,f)) and sys.argv[0] not in f and "README" not in f and "readme" not in f:
			files.append(join(dir,f))
		elif sys.argv[0] not in f and "README" not in f and "readme" not in f:
			listFiles(join(dir,f))

listFiles("./")

for f in files:
	file = open(f,"r")
	data = file.read()
	res = re.findall("TODO:(.*?)\n", data)
	lines = re.split("\n", data)
	for i  in range(len(res)):
		for u in range(len(lines)):
			if res[i] in lines[u]:
				res[i] = f+" l: "+str(u+1)+" "+res[i]
				break
	matchs = matchs + res;
	file.close()

#ecriture des  resultats
file = open(os.path.join("./","README.md"), "r")
data = file.read()
file.close()
file = open(os.path.join("./","README.md"), "a+")
for entry in matchs:
	if entry not in data:
		file.write("- [ ] "+entry+"\n")

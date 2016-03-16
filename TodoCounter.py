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
	print "Recherche dans "+f
	file = open(f,"r")
	data = file.read()
	res = re.findall("TODO:(.*?)\n", data)
	lines = re.split("\n", data)
	for i  in range(len(res)):
		for u in range(len(lines)):
			if res[i] in lines[u]:
				print "    Entrée trouvée ligne "+str(u+1)
				ft = f
				#Eventuellement remplacer master par branche actuelle
				ft = "blob/master"+ft.replace(".","", 1)
				res[i] = "["+f+"]("+ft+") l: "+str(u+1)+" "+res[i]
				break
	matchs = matchs + res;
	file.close()

#ecriture des  resultats
file = open(os.path.join("./","README.md"), "r")
data = file.read()
file.close()
file = open(os.path.join("./","README.md"), "w+")
txt = ""
for entry in matchs:
	print "Ecriture de "+entry
	testEntry = entry.replace("\\", "/")
	txt = txt + "- [ ] "+testEntry+"\n"
print "Texte à écrire\n"+txt
txt = "[Clutter]\n"+txt+"[/Clutter]"
data = re.sub("\[Clutter\]\n*(.*)\n*\[\/Clutter\]", txt, data, flags=re.DOTALL)
print "Texte final \n"+data
file.write(data)
file.close()
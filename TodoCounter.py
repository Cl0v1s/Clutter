import sys
import re 

if len(sys.argv):
	print "Vous devez preciser un fichier a analyser"
	exit()

try:
	file = open(sys.argv[1],"r")
except IOError: 
	print "Impossible de lire le fichier a analyser."
	exit()
data = file.read()
matchs = re.findall("TODO:(.*?)\n", data)
file.close()
file = open("README.md", "a+")
data = file.read()
for entry in matchs:
	if entry not in data:
		file.write("- [ ]:"+entry+"\n")

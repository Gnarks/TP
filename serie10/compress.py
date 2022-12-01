"""
Usage:
	compress -t <tech> (-c | -d) --in=<FICHIER> [--out=<FICHIER>]
	compress -h | --help
Options:
	-h --help 			Montrer l'aide
	-c        			Activer la compression
	-d       			Activer la décompression
	-t <tech>			technique de (dé)compression (LZ ou ADN)
	--in <FICHIER>		Fichier d'entrée
	--out <Fichier>	Fichier de sortie (ou choisi automatiquement si pas spécifié)
"""
from docopt import docopt

class BadAdnFormat(Exception):
    pass

def comp_LZ(fin,fout):
    if fout =="":
        fout = f"out{fin}"
    liste = []
    with open(fin,"r") as f:
        liste = f.readline().strip("\n").split(" ")
    word_list = []
    string = ""
    for word in liste:
        if word not in word_list:
            word_list.append(word)
        string += f"{word_list.index(word)}"
    dic = ""
    for elem in word_list:
        print(elem)
        dic+= f"{elem};"
    with open(fout,"w") as f:
        f.write(f"{string}\n{dic}")

def comp_RLE(fin,fout):
    if fout =="":
        fout = f"out{fin}"
    liste = []
    with open(fin,"r") as f:
        adn = "actg"
        for line in f.readlines():
            for elem in line.strip("\n"):
                if elem not in adn:
                    raise BadAdnFormat
                liste.append(elem)
    string =""
    empty =""
    i=0
    while i < len(liste):
        compt = 1
        while i + 1 < len(liste) and liste[i] == liste[i+1]:
            compt+= 1
            i+=1
        string += f"{compt if compt!=1 else empty}{liste[i]}"
        i+=1
    with open(fout,"w") as f:
        f.write(string)
        
def decomp_LZ(fin,fout):
    if fout =="":
        fout = f"out{fin}"
    with open(fin,"r") as f:
        base_string = f.readline().strip("\n")
        word_list = f.readline().split(";")
        print(base_string)
        print(word_list)
    string = ""
    for nbr in base_string:
        string+= f"{word_list[int(nbr)]} "
    with open(fout,"w") as f:
        f.write(f"{string}")

def decomp_RLE(fin,fout):
    if fout =="":
        fout = f"out{fin}"
    with open(fin,"r") as f:
        base_string = str(f.readlines()).strip("\n").strip("[").strip("]").strip("'")
    string =""
    i=0
    while i < len(base_string):
        if base_string[i] in "1234567890":
            total = base_string[i]
            while base_string[i+1] in "1234567890":
                total+=base_string[i+1]
                i+=1
            string+=  f"{base_string[i+1]}" * int(total)
        else:
            string+=base_string[i]
        i+=1
    with open(fout,"w") as f:
        f.write(string)
        
    
    
decomp_RLE("outtest.txt","translate.txt")
"""args = docopt(__doc__, version="compress 0.42")
if args["-c"]:
	if args["-t"] == "LZ":
		comp_LZ(args["--in"], args["--out"])
	elif args["-t"] == "ADN":
		comp_RLE(args["--in"], args["--out"])
	else:
		exit(__doc__)
"""
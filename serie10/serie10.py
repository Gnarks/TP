"""Usage :
  compress.py (-c|-d) -t <technique> --in <fichier> [--out <fichier>]
  
Options:
  -h --help     Show this screen.
  --version     Show version.
  -c            compress the following file.
  -d            decompress the following file.
  -t <technique>technique that'll be used.
  --in          entry file.
  --out         exit file.
"""
from docopt import docopt

args = docopt(__doc__)


unelist = ["oui","non","(","(","oui","non","2"]

def lZ(liste):
    word_list = []
    string = ""
    for word in liste:
        if word not in word_list:
            word_list.append(word)
        string += f"{word_list.index(word)}"


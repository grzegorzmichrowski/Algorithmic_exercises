import sys

import string
    
vowel = {"a", "e", "i", "o", "u"}
consonant = set(string.ascii_lowercase) - vowel
    

if(len(sys.argv)>=2):
    for i in range(len(sys.argv[1:])):
        verb_minus_1ch = sys.argv[1:][i][:-1]
        if sys.argv[1:][i].endswith("w" or "x" or "y"): # change to sys.argv......('w') or sys.argv.....('x').......
            print(sys.argv[1:][i]+"ing")
        elif (verb_minus_1ch[-1:] in vowel) and (sys.argv[1:][i][-1:] in consonant):
            print(sys.argv[1:][i][:-1]+(2*sys.argv[1:][i][-1:])+"ing")
        elif sys.argv[1:][i].endswith("ee"):
            print(sys.argv[1:][i]+"ing")
        elif sys.argv[1:][i].endswith("ie"):
            print(sys.argv[1:][i][:-2]+"ying")
        elif sys.argv[1:][i].endswith("e"):
            print(sys.argv[1:][i][:-1]+"ing")
        else:
            print(sys.argv[1:][i]+"ing")

# change sys.argv[1:] to nice variable

    #są jeszcze wyjątki czasowników dwusylabowych z akcentem na pierwszą sylabę, w których nie dodajemy dodatkowej litery pomimo tego ze mamy vowel i consonent na końcu
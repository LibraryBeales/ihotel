import os, glob
files = glob.glob("*.txt")

with open("000merged.txt", "w") as outfile:
    alllines = []
    for f in files:
        with open(f,'r') as infile:
            alllines.append(infile.read())
        alllines = set([line.strip() for line in alllines])
    for item in alllines:
        outfile.write(item + '\n')

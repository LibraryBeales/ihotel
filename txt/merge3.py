from glob import glob
output = open("allchapters.txt", "w")
#output.write("state,sex,year,name,count\n")
for fname in glob("*.TXT"):
    print("Adding", fname)
    f = open(fname)
    output.write(f.read())
    f.close()
output.close()

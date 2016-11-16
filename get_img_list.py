import os
dir = "D:\\maching_learning\\Caltech101\\101_ObjectCategories\\101_ObjectCategories"
wildcard = ".jpg"
recursion = 1
label = -1
outfile = "train.txt"
file = open(outfile,"w")
exts = wildcard.split(" ")
for root,subdirs,files in os.walk(dir):
    #print root
    #print subdirs
    label = label + 1
    for name in files:
        for ext in exts:
            if(name.endswith(ext)):
                file.write(root +"\\"+name + " "+str(label)+"\n")
                break
        if(not recursion):
            break

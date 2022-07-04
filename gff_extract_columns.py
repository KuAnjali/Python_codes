#!/usr/bin/python
import re
inFile=open('B0P1.gff').readlines()
count=0
occurence=[]
for line in inFile:
        if line.startswith("#"):
                continue
        else:
                line=line.strip("\n")
                line=line.split("\t")
                info=line[8]
                if "ID=transcript;Parent=gene:" in info:
                        geneName=info.split(";")
                        Locus=geneName[1].split(":")[1]
                print(re.findall(Locus, info))


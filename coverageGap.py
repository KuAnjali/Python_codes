##To identify the coverage gaps of length 150 or greater from the input file (chr, start., end)

#!bin/python
import sys,csv
i=0
outFile=open(sys.argv[2],"a")
tsv_file = open(sys.argv[1])
sampleName = sys.argv[3].split(".")[0]
read_tsv = csv.reader(tsv_file, delimiter="\t")
#print(read_tsv.len())
count = len(open(sys.argv[1]).readlines())
#print(count)
#exit(0)
gapStart=0
rowCount=0
result=[]
for row in read_tsv:
	#print(row)
	rowCount=rowCount+1
	if(row[3]==str(0) and gapStart==0):

		gapStart=1
		gapStartVal=row[1]
		gapStartRow=rowCount
	if(row[3]==str(0)):
		i=i+1
		gapEndVal=row[2]
		gapEndrow=rowCount
		if(rowCount==count):
			if(i>=150):
				res=[sampleName,gapStartVal,gapEndVal]
				result.append(res)
		
	else:
		if(i>=150):
			res=[sampleName,row[0],gapStartVal,gapEndVal]
			result.append(res)
		gapStart=0
		i=0
	
print(result)
with outFile:
    write = csv.writer(outFile)
    write.writerows(result)

#!/usr/bin/python
import sys
#print(sys.argv)

fastafile=sys.argv[1]
mergedname=sys.argv[2]
fastaoutput=sys.argv[3]

#def merge_fasta(fastafile, mergedname, fastaoutput):
fasta=open(fastafile)
fasta2=open(fastaoutput,"w")
fasta2.write(">"+mergedname+"\n")
for line in fasta:
    if line.startswith(">"):
        print("merging "+line)        
    else:
        fasta2.write(line.replace("\n",""))
fasta2.close()

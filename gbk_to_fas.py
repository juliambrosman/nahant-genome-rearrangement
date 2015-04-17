#!/usr/bin/python

import sys
from Bio import SeqIO
import re
from Bio.SeqFeature import FeatureLocation

list_of_files=sys.argv[1]

def cds_gbk_extract(list_of_files):
    gbkfiles=open(list_of_files)
    genbankfiles=gbkfiles.readlines()
    for line in genbankfiles:
        filename=line.replace(".gbk\n","")
        cdsfna=open(filename+".fna", "w")
        cdsfaa=open(filename+".faa", "w")
        gbk=line.replace("\n","")
        SeqIO.convert(gbk, "genbank", filename+".genome.fasta", "fasta")
        for rec in SeqIO.parse(gbk, "genbank"):    
            for feature in rec.features:
                if feature.type=="CDS":
                    name=str(feature.qualifiers["locus_tag"])#+"_"+str(feature.qualifiers["product"])
                    local=feature.location                 
                    na=feature.location.extract(rec).seq   
                    aa=str(feature.qualifiers["translation"])
                    aa=aa.replace("[","").replace("]","").replace("'","")
                    cdsfna.write(">"+str(name)+"\n"+str(na)+"\n")
                    cdsfaa.write(">"+str(name)+"\n"+str(aa)+"\n")
        cdsfna.close()
        cdsfaa.close()    

cds_gbk_extract(list_of_files)
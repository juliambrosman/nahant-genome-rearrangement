#!/usr/bin/python
#Write a list of tasks to do the first round assembly for a list of fastq read files
import sys

fastq_list=sys.argv[1]

def step1_script(fastq_list):
    fastq=open(fastq_list)
    program=open("step1.sh","w")
    for name in fastq:
        vec=name.split("_")
        heading=vec[0]
        program.write("\n\n#"+name+"\nclc_assembler -o "+heading+"step1.clc.fasta -m 500 -p fb ss 100 300 -q "+ name+"\nclc_mapper -o "+heading+"step1.cas -p fb ss 100 300 -q "+name.replace("\n","")+" -d "+heading+"step1.clc.fasta -a local -r ignore\nclc_cas_to_sam -a "+heading+"step1.cas -o "+heading+"step1.bam\n\nsamtools sort "+heading+"step1.bam 1.025.O.sorted\nsamtools index "+heading+"sorted.bam\nbedtools genomecov -ibam "+heading+"step1.bam -d >"+heading+"step1.genomecoverage.txt")
    program.close()

step1_script(fastq_list)
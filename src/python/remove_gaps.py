'''
I am going to remove the gaps here

idk if its a good idea

'''
from Bio.SeqIO.FastaIO import FastaIterator
import argparse

parser = argparse.ArgumentParser(
    description = "removes gaps from fasta"
)

parser.add_argument (
    "-f", "--file"
)

args = parser.parse_args()

with open(args.file) as handle:
    for record in FastaIterator(handle):
        seq = record.seq
        cleaned = seq.replace("-", '')
        print (f">{record.id}")
        print(cleaned)

'''
Now that the gaps are removed,
we can translate and get the AA seq
'''
from Bio import SeqIO

from Bio.SeqIO.FastaIO import FastaIterator
import argparse

parser = argparse.ArgumentParser(
    description = "translates gap-free fasta"
)

parser.add_argument (
    "-f", "--file"
)

args = parser.parse_args()

with open(args.file) as handle:
    for record in FastaIterator(handle):
        translated_seq = record.seq.translate()
        print (f">{record.id}")
        print(f"{translated_seq}")



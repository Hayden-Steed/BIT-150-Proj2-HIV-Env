'''
Initially we might have a problem.

Due it its high mutation rate, the Env gene has many gaps. This program is to play around
with the gaps I'm seeing and try to see if there are any regularities. It sums up where
gaps are NOT detected for each fasta reference per column. It outputs each column
horizontally on a new line. 

ex: 

    1234
    1 // gap here among most seq
    1
    1231  // no gap among most seq
    1413
    1341
    1413

'''

from Bio.SeqIO.FastaIO import FastaIterator
import argparse

parser = argparse.ArgumentParser(
    description = "prints overview of gaps in fasta"
)

parser.add_argument (
    "-f", "--file"
)

args = parser.parse_args()

print(f"file '{args.file}' ")

# HARDCODED
# this is not for general use, varying sequence lengths will
# break this program
length = 9332

# should be around 9.3 kb, a lot of ram, but okayish
# it does however speek to the speed of the program, unfortunately
cols = [0] * length
seq_count = 0

with open(args.file) as handle:
    for record in FastaIterator(handle):
        seq = record.seq
        seq_length = len(record.seq)
        
        col_i = 0
        for nuc in seq:
            if nuc != '-':
                cols[col_i] += 1
            col_i += 1
        
        seq_count += 1

for act_place in cols: 
    print(f"{act_place}")

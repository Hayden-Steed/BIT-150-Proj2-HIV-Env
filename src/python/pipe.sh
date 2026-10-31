#!/bin/bash

data_file_path=$1

file_name="${data_file_path##*/}"    
root_name="${file_name%%.*}"

# ex: ../../data/

dest_folder=$2

stripped_path="$dest_folder$root_name-no-gaps.fasta"

python3 remove_gaps.py -f $data_file_path >$stripped_path

translated_path="$dest_folder$root_name-trans.faa"

python3 translate_seq.py -f $stripped_path >$translated_path

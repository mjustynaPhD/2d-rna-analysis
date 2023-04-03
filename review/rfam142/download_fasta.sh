#!/bin/bash

LINK=https://ftp.ebi.ac.uk/pub/databases/Rfam/14.2/fasta_files/
LAST=3125

# iterare over indece 1 to 3125 and download the fasta files from RF00001 to RF03125
for i in $(seq -f "%05g" 1 $LAST)
do
    echo $i
    wget $LINK/RF$i.fa.gz
done

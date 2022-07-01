#!/bin/bash

FASTA="/data/2d-rna/pseudoknots-bpseqs"
CSV="/data/2d-rna/rnapdbee-cifs"
OUTPUT="/data/2d-rna/pseudoknots-bpseqs/"

for f in $FASTA/*.dbn
do
    # echo $f
    base=${f/$FASTA}
    base=${base/.dbn}
    echo $base

    cp $CSV/$base/0/whole.bpseq $OUTPUT/$base.bpseq

done
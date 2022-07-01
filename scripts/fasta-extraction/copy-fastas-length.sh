#!/bin/bash

FASTA="/data/2d-rna/fasta-cifs"

for f in $FASTA/*.fa
do
    echo $f
    length=`tail -1 $f | wc -m`
    if [[ "$length" -lt 1000 ]]
    then
        cp $f /data/2d-rna/fasta1000/
    fi

    # if [[ "$length" -lt 600 ]]
    # then
    #     seq=${f/.fa/.seq}
    #     cp $seq /data/2d-rna/fasta600/
    # fi

    # if [ "$length" -gt 600 ] && [ "$length" -lt 1800 ]
    # then
    #     seq=${f/.fa/.seq}
    #     cp $seq /data/2d-rna/fasta600-1800/
    # fi

done
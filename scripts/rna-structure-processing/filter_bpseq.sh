#!/bin/bash

PREDS="/data/2d-rna/rna-structure-bpseqs"
TARGETS="/data/2d-rna/rna-struct-validation/all"
OUTPUT="/data/2d-rna/rna-struct-validation/all"

for id in $PREDS/7*;
do
    if [[ -d $id ]]
    then
        raw_id=${id/$PREDS}
        for method in $id/*;
        do
            dir=${method/$id}
            dir=${dir:1}
            if [ $dir != "Target" ]
            then
                target=$TARGETS/$raw_id/Target/*.bpseq
                control=$PREDS/$raw_id/$dir/0/whole.bpseq
                echo $control
                python3 filter_bpseqs.py $target $control $OUTPUT/$raw_id/$dir
            fi
        done
    fi
    
done

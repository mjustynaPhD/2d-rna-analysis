#!/bin/bash

PREDS="/data/2d-rna/new-cifs/predictions-bpseqs"
TARGETS="/data/2d-rna/new-cifs/validation-all"
OUTPUT="/data/2d-rna/new-cifs/validation-all"
method="rna-structure"

for id in $PREDS/*;
do
    if [[ -d $id ]]
    then
        raw_id=${id/$PREDS}

        dir=${method/$id}
        echo $dir
        if [ $dir != "Target" ]
        then
            target=$TARGETS/$raw_id/Target/*.bpseq
            control=$PREDS/$raw_id/$dir/0/whole.bpseq
            echo $control
            python3 filter_bpseqs.py $target $control $OUTPUT/$raw_id/$dir
        fi
        
    fi
    
done

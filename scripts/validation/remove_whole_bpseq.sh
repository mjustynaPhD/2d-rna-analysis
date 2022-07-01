#!/bin/bash

P="./*"
for id in $P;
do
    if [[ -d $id ]]
    then
        for method in $id/*;
        do
            dir=${method/$id}
            dir=${dir:1}
            if [ $dir != "Target" ]
            then
                # echo $dir/whole.bpseq
                # echo $id/Target/*.bpseq
                echo $id/$dir/whole.bpseq
                sudo rm -rf $id/$dir/whole.bpseq
            fi
        done
    fi
    
done

#!/bin/bash
# Read a list of ids from stdin and copy the corresponding files from directory $1 to directory $2
# Usage: cat ids.txt | copy-by-id.sh /path/to/source /path/to/destination
# Example:  cat ../../data/test-set-2-ids-all.txt | copy-by-id.sh /data/2d-rna/new-cifs/validation-all /data/2d-rna/2d-rna-analysis/data/test-set-2-bpseq

while read id; do
    echo $id
    nid=${id:0:4}
    end=${id:5:4}
    
    # id_=$id"_*_"$end
    echo $nid"_"?"_"$end
    cp $1/$nid"_"*"_"$end/Target/*.bpseq $2
done







    

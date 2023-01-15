#!/bin/bash
# Read a list of ids from stdin and copy the corresponding files from directory $1 to directory $2
# Usage: cat ids.txt | copy-by-id.sh /path/to/source /path/to/destination

while read id; do
    echo $id
    id=${id:0:4}
    end=${id:6:2}
    cp $1/$id_?_$end/Target/*.bpseq $2
done







    

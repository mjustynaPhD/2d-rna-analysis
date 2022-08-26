#!/bin/bash
INPUT="/data/2d-rna/new-cifs/rna-struct-validation/"
OUTPUT="/data/2d-rna/new-cifs/validation-all/"
NAMES=`cat best-new-cifs.txt`

for f in $NAMES
do
    echo $f
    
    # echo $f | grep -aob "/"
    index=`echo $f | grep -aob "/" | grep -oE '[0-9]+'`
    # echo $index
    out=${f:0:$index}
    echo $OUTPUT/$out/rna-structure/
    mkdir -p $OUTPUT/$out/rna-structure
    cp $INPUT/$f/*.bpseq $OUTPUT/$out/rna-structure/
    # cp $CSV/$base/0/whole.bpseq $OUTPUT/$base/Target

done

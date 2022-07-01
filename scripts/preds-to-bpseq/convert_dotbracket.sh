#!/bin/bash

DATA=$1

for f in $DATA/*.out
do
    echo $f
    out=${f/.out/.dbn}
    head -2 $f > $out
    tail -1 $f >> $out

done
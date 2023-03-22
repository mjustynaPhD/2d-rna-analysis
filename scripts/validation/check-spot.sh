#!/bin/bash

P="./spot-rna/"

for f in $P/*.bpseq ; do
    cat $f | awk '{ print $1; }' | sort | uniq -c | awk '{print $1;}' | sort | uniq | awk '{if ($1 > 1) print "YES"; else print "NO";}'
done
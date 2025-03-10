#!/bin/bash

# Add .bpseq extension to all files in a directory given by argument

for file in $1/*; do
    mv $file $file.bpseq
done


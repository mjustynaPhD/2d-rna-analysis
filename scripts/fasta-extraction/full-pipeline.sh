#!/bin/bash

echo "AWK Charge"
#./awk-charge-pipeline.sh
echo "Python preprocess"
#./python-preprocess-pipeline.sh
echo "RNAPDBEE"
./rnapdbee-pipeline.sh
echo "DBN extraction"
./awk-extract-dbn-pipeline.sh
echo "Fasta extraction"
./fasta-extract-pipeline.sh

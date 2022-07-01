#!/bin/bash

cd /home/macieka/2d-analysis
DATA="/data/2d-rna/rnapdbee-cifs"
OUT="/data/2d-rna/dbn-cifs"
mkdir $OUT

for f in $DATA/*
do
    inp_name=$f/0/whole.dbn
    out_name=${f/$DATA/$OUT}.dbn
    m_id=${out_name/$OUT}
    m_id=${m_id/.dbn}
    m_id=${m_id:1}
    # echo $out_name
    # echo $m_id
    /usr/bin/gawk -v molecule_id=$m_id -f extract-2d.awk < $inp_name > $out_name

done

#! /bin/bash

for f in $1/*
do
    
    if [ -d $f ]
    then
        # echo $f
        res=`cat $f/Target/*.bpseq | awk '{print $3;}' | sort | uniq | wc -l `

        
        if [ "$res" -eq "1" ]
        then
            echo $f
            sudo rm -rf $f
        fi
    

    fi

done

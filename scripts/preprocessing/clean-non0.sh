#! /bin/bash

# Remove structures with no base pairs

for f in $1/*
do
    
    if [ -d $f ]
    then
        # echo $f
        res=`cat $f/0/whole.bpseq | awk '{print $3;}' | sort | uniq | wc -l `

        
        if [ "$res" -eq "1" ]
        then
            echo $f $res
            sudo rm -rf $f
        fi
    

    fi

done

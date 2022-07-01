from enum import unique
import os
import sys
from tqdm import tqdm

input_path= sys.argv[1]
files = os.listdir(input_path)
uniq_files = [f for f in files if f.endswith(".dbn")]
uniq_files = [f.replace(".dbn", "") for f in uniq_files]


def filter_bpseq(dots, bpseq):
    out_bp = []
    ignore = ['.', '[', ']']
    for a in range(len(dots)):
        if dots[a] not in ignore:
            b = bpseq[a].split()
            b[2] = "0\n"
            bpseq[a] = " ".join(b)
    return bpseq

def save_new_bpseq(bpseq, name):
    name = name +"-new.bpseq"
    with open(os.path.join(input_path, name), 'w') as f:
        f.writelines(bpseq)    


for f in tqdm(uniq_files):
    
    with open(os.path.join(input_path, f+".dbn")) as sf:
        dots = sf.readlines()[-1].strip()

    with open(os.path.join(input_path, f+".bpseq")) as bf:
        bpseq = bf.readlines()

    filter_bpseq(dots, bpseq)
    save_new_bpseq(bpseq, f)
import os
import sys
import shutil
from tqdm import tqdm

input_path = sys.argv[1]
output_path = "/data/2d-rna/new-cifs/pseudoknots-bpseqs/"
print(input_path)

files = os.listdir(input_path)
print(len(files))

pseudo_seqs = []

for a in tqdm(files):
    with open(os.path.join(input_path, a)) as f:
        seq = f.readlines()[-1]
        if '[' in seq:
            pseudo_seqs.append(a)

print(len(pseudo_seqs))
for a in tqdm(pseudo_seqs):
    shutil.copy(os.path.join(input_path, a), os.path.join(output_path, a))

        

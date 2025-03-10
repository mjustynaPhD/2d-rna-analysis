import os
from functools import partial
from multiprocessing import Pool
import numpy as np
from tqdm import tqdm

O = "/home/mjustyna/2d-rna-analysis/data/test-set-2-fasta/"
P = "single_seed_fastas/"
neobio_path = "/home/mjustyna/software/bin/"
# for p in os.scandir(P):
#     print(p)
COUNTER = 0
D = os.listdir(P)
def compare(f1):
    global COUNTER, D
    # os.system(f"./compare_shell.sh {O}/{f1} {P}/{f2}")
    print(COUNTER, f1)
    COUNTER += 1
    for f2 in tqdm(D):
        neobio_run = f"neobio.textui.NeoBio NW {O}/{f1} {P}/{f2}"
        # print(f1, f2)
        o = os.popen(f"java -cp {neobio_path} {neobio_run} 2>/dev/null | tail -4").read()
        out = o.split('\n')
        seq = len(out[0].replace("-",""))
        aln = out[1].count("|")
        seq2 = len(out[2].replace("-",""))
        seq_len = max(seq, seq2)
        sim = aln/seq_len
        # print(f1, f2, sim)
        if sim >= 0.8:
            os.system(f"touch exp2_2/{f1}_{f2}-sim_{sim:.2f}.txt")
            return True

if __name__ == "__main__":
    np.random.seed(42)
    np.random.shuffle(D)
    F = os.listdir(O)[150:]
    with Pool(64) as pool:
        pool.map(compare, F)
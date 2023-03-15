import os
from functools import partial
from multiprocessing import Pool

O = "/home/mjustyna/2d-rna-analysis/data/test-set-2-fasta/"
P = "samples/"
neobio_path = "/home/mjustyna/software/bin/"
# for p in os.scandir(P):
#     print(p)

def compare(f1, f2):
    neobio_run = f"neobio.textui.NeoBio NW {P}/{f1} {O}/{f2}"
    print(f1, f2)
    o = os.popen(f"java -cp {neobio_path} {neobio_run} | tail -2").read()
    out = o.split('\n')
    seq = len(out[0].replace("-",""))
    aln = out[1].count("|")
    seq2 = len(out[2].replace("-",""))
    seq_len = max(seq, seq2)
    sim = aln/seq_len
    # print(f1, f2, sim)
    if sim >= 0.8:
        os.system(f"touch exp2_2/{f1}_{f2}-sim_{sim:.2f}.txt")

if __name__ == "__main__":
    # for f1 in os.listdir(P):
    #     for f2 in os.listdir(O):
    #         compare(f1, f2)
    #         break
    #     break
    for f in os.listdir(O):
        func = partial(compare, f2=f)
        with Pool(64) as pool:
            pool.map(func, next(os.walk(P))[2])
        
        
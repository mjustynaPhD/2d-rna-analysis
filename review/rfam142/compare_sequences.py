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
    s_len = len(out[0])
    score = int(out[1].split(' ')[-1])
    if score/s_len >=0.8 1:
        os.system(f"touch out/{f1}_{f2}")

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
        
        
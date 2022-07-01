from cmath import e
import os


target_bpseq_path = "/data/cif/eltetrado/"
dst_path = "./"

different = []

def move_and_compare(target_path, dst_path):
    target_files = os.listdir(target_path)
    target_files = [t for t in target_files if t.endswith(".bpseq")]
    target_ids = [t[:4].upper() for t in target_files]
    ids_names = dict([(i, n) for i, n in zip(target_ids, target_files)])
    dst_dirs = os.listdir(dst_path)
    dst_dirs = [d for d in dst_dirs if os.path.isdir(os.path.join(dst_path, d))]
    for d in dst_dirs:
        compare_sequences(d, ids_names, target_path, dst_path)

def compare_sequences(dir, ids_names, target_path, dst_path):
    id_path = os.path.join(dst_path, dir)
    methods = os.listdir(id_path)
    try:
        target_seq = read_seq(target_path, ids_names[dir])
        # print(target_seq)
    except KeyError:
        print(dir, "json does not extist!")
        return
    for m in methods:
        method_path = os.path.join(id_path, m)
        seq = read_seq(method_path, name="whole.bpseq")
        if seq != target_seq:
            print(dir, "seq is diffetent!")
            print("Target: ", target_seq)
            print("Tested: ", seq)
            print("Method: ", m)
            different.append(dir)
            return

def read_seq(path, name):
    try:
        f = open(os.path.join(path, "0", name))
    except FileNotFoundError:
        f = open(os.path.join(path, name))
    finally:
        bpseq = f.readlines()
        f.close()
    seq_dict = dict([(int(b.split()[0]), b.split()[1]) for b in bpseq])
    seq=''
    for a in range(len(seq_dict)):
        seq+=seq_dict[a+1]
    return seq


if __name__ == "__main__":
    move_and_compare(target_bpseq_path, dst_path)
    print(len(different))
    print(different)

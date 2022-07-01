"""
ID
|- Target
|- spot-rna
"""
import os
import sys
import shutil
target_path="/data/2d-rna/predictions-bpseqs/"
structure_path="/data/2d-rna/val-test/"

def create_structure(files, structure_path, name="Target"):
    names = [f[:4].upper() for f in files]
    for n in names:
        id_path = os.path.join(structure_path, n, name)
        if not os.path.exists(id_path):
            os.makedirs(id_path)
    
def copy_targets(files, src_path, dst_path):
    for f in files:
        name = f[:4].upper()
        src = os.path.join(src_path, f)
        dst = os.path.join(dst_path, name, "Target", f)
        shutil.copy(src, dst)

def copy_methods(targets, src_path, dst_path):
    methods = os.listdir(src_path)
    methods = [f for f in methods if os.path.isdir(os.path.join(src_path, f))]
    for m in methods:
        create_structure(targets, dst_path, m)
        methods_files = os.listdir(os.path.join(src_path, m))
        methods_files = [m for m in methods_files if m.endswith("-new.bpseq")]
        for f in methods_files:
            name = f[:4].upper()
            src = os.path.join(src_path, m, f)
            dst = os.path.join(dst_path, name, m, f)
            shutil.copy(src, dst)


if __name__=="__main__":
    targets = os.listdir(target_path)
    targets = [t for t in targets if t.endswith('.bpseq')]
    create_structure(targets, structure_path, "Target")
    # copy_targets(targets, target_path, structure_path)
    copy_methods(targets, target_path, structure_path)


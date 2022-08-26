import os
import sys

reference = sys.argv[1]
control = sys.argv[2]
output_path = sys.argv[3]

def read_bpseq(path):
    with open(path) as f:
        lines = f.readlines()
    lines = [l for l in lines if not l.startswith("#")]
    return lines

def create_bpseq(ctrl_lines, common):
    out = []
    for l in ctrl_lines:
        l = l.split()
        if int(l[0]) not in common and int(l[2]) not in common:
            l[2] = '0'
        l.append("\n")
        out.append(" ".join(l))
        
    return out

def save_bpseq(path, name, bpseq):
    if not os.path.exists(path):
        os.makedirs(path)
    
    with open(os.path.join(path, name), 'w') as f:
        f.writelines(bpseq)


# print(reference, control)
ref_lines = read_bpseq(reference)
ctrl_lines = read_bpseq(control)
ref_ids = set([int(r.split()[0]) for r in ref_lines if r.split()[2].strip()!='0'])
ctrl_ids = set([int(r.split()[0]) for r in ctrl_lines if r.split()[2].strip()!='0'])

filtered = ref_ids.intersection(ctrl_ids)
# print(filtered)
bpseq = create_bpseq(ctrl_lines, filtered)
bname = os.path.basename(control)
save_bpseq(output_path, bname, bpseq)

import sys
import os
OUTPUT_PATH="/data/2d-rna/predictions-rna-structure/"
inp_file = sys.argv[1]

with open(inp_file) as f:
    lines = f.readlines()
inp_file = os.path.basename(inp_file)
seq = lines[1]
for a in range(2, len(lines), 2):
    out_file = inp_file.replace(".dot", "-"+str(int((a-2)/2))+".dot")
    dir_name = inp_file.replace(".dot", "")
    if not os.path.exists(os.path.join(OUTPUT_PATH, dir_name)):
        os.makedirs(os.path.join(OUTPUT_PATH, dir_name))
    
    with open(os.path.join(OUTPUT_PATH, dir_name, out_file), 'w') as f:
        if a==2:
            f.write(lines[0])
            # print(lines[0])
        else:
            f.write(lines[a-1])
            # print(lines[a-1])
        f.write(seq)
        f.write(lines[a])
        # print(seq)
        # print(lines[a])
    # print(int((a-2)/2))
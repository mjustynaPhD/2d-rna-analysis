import os
files = os.listdir("./")
files = [f for f in files if f.endswith(".fa")]

for f in files:
    print(f)
    with open(f) as fa:
        lines= fa.readlines()
    lines[1]=lines[1].upper().replace("T", "U")
    seq_file = f.replace(".fa", ".seq")
    with open(seq_file, 'w') as fa:
        fa.write(lines[1])
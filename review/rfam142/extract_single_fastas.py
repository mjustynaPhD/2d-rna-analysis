import os
from multiprocessing import Pool

# for each fasta file in the fasta_files directory extract fasta sequences and store each of them in a separate file
# the name of the file is the name of the fasta sequence
def extract_single_fastas(fastas):
    for file in [fastas]:
        if file.endswith(".fa"):
            with open("fasta_files/" + file, "r") as f:
                lines = f.readlines()
                for i in range(0, len(lines)):
                    print(f"{i}_{file}")
                    if lines[i].startswith(">"):
                        p = f"single_fasta/{i}_{file}"
                        if not os.path.exists(p):
                            with open(p, "w") as f2:
                                f2.write(lines[i])
                                f2.write(lines[i + 1])

if __name__ == '__main__':
    # multiprocessing pool
    fastas = os.listdir("fasta_files")
    print(len(fastas))
    with Pool(12) as pool:
        pool.map(extract_single_fastas, fastas)
    # extract_single_fastas(fastas)
import os
import shutil
import sys


# read source and destination paths from command line
src = sys.argv[1]
dst = sys.argv[2]

# read ids from file given in argument
ids = []
with open(sys.argv[3]) as f:
    ids = f.readlines()
    ids = [i.strip() for i in ids]



# get all files in source directory
files = os.listdir(src)

# remove pattern '_?_' from a string
def remove_pattern(s):
    # return s[:4] + s[6:]
    # return s[:4] + s[6:].replace('.fa', '')
    return s.replace('.fa', '')

def map_paths(files):
    mapping = {}
    for f in files:
        f_new = remove_pattern(f)
        mapping[f_new] = f
    return mapping
    
if __name__ == '__main__':
    map_files = map_paths(files)
    for i in ids:
        try:
            # shutil.copyfile(os.path.join(src, map_files[i], 'Target/', f'{map_files[i]}.bpseq'), os.path.join(dst, map_files[i]))
            
            p = os.path.join(src, f'{map_files[i]}')
            print(p)
            shutil.copyfile(p, os.path.join(dst, map_files[i]))
        except:
            print(f'File {i} not found')
    # print(map_files)
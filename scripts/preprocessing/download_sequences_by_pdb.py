import os
from rna2d.utils import download_pdbs# , extract_sequences, extract_2d_structure


input_files = [
    '4XW7',
    '6POM',
    '6Y0Y',
    '8HB8',
    '7V9E',
    '7ELP',
    '5T5A',
    '7EOJ',
    '7MLX',
    '5DI4',
    '5K7C',
    '4L81',
    '7BG9',
    '3OWZ',
    '6TB7',
    '8GXC',
    '4P9R',
]

if __name__ == "__main__":
    out_path = 'noncanon'
    os.makedirs(out_path, exist_ok=True)
    download_pdbs(input_files, f'{out_path}/pdb_files')
    # extract_sequences(input_files, f'{out_path}/pdb_files', f'{out_path}/sequences')
    # extract_2d_structure(input_files, f'{out_path}/pdb_files', f'{out_path}/2d_structures')   
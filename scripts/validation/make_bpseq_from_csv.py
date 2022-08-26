
import sys
import os
from typing import Dict, List, Tuple, Union


def conversion_pipeline(csv, fasta, cif, output_path, wobble: bool = True):
    sequence, bpseq = convert_to_bpseq(csv, fasta, cif, wobble=wobble)
    bname = os.path.basename(fasta).replace(".fa", ".bpseq")
    save_bpseq(os.path.join(output_path, bname), bpseq, sequence)


def convert_to_bpseq(csv, fasta, cif, wobble: bool = True) -> Tuple[str, Dict[int, List]]:
    lines = read_csv_lines(csv)
    sequence = get_sequence(fasta).upper()
    joined_ids, bpseq = get_residues_ids(csv, cif, sequence, label_seq_id=False)
    try:
        bpseq = make_bpseq_structure(
            sequence, lines, bpseq, joined_ids, wobble)
    except KeyError as e:
        joined_ids, bpseq = get_residues_ids(csv, cif, sequence, label_seq_id=True)
        bpseq = make_bpseq_structure(
            sequence, lines, bpseq, joined_ids, wobble)

    return sequence, bpseq

def get_residues_ids(csv, cif, sequence, label_seq_id:bool):
    seq_cif, joined_ids = get_cif_sequence_ids(cif, label_seq_id=label_seq_id)
    if seq_cif != sequence:
        print(csv, len(seq_cif), len(sequence))
    bpseq: Dict[int, List] = {}
    for a in range(len(sequence)):
        bpseq[a+1] = []
    return joined_ids, bpseq


def make_bpseq_structure(sequence: str, lines: list, bpseq: dict, joined_ids: Dict[str, int], wobble: bool = True) -> Dict[int, List]:
    wobble_pairing = {'GU', 'UG'}
    for l in lines:
        lfields = [x.strip() for x in l]
        try:
            lfields = residue_to_upper_case(lfields)
        except ValueError as e:
            print(lfields)
            raise
        pair = get_pair_by_ids(lfields, sequence, joined_ids)
        if not wobble and pair in wobble_pairing:
            continue
        bpseq[joined_ids[lfields[0]]].append(joined_ids[lfields[1]])
        bpseq[joined_ids[lfields[1]]].append(joined_ids[lfields[0]])
    for v in bpseq.values():
        if len(v) == 0:
            v.append(0)
    return bpseq


def residue_to_upper_case(lfields):
    # B.u1
    c1, r1 = lfields[0].split('.')
    c2, r2 = lfields[1].split('.')
    # u-> upper()
    # B.U1

    def convert(r):
        aa = r[0].upper()
        rest = r[1:]
        return aa, rest
    aa1, rest1 = convert(r1)
    aa2, rest2 = convert(r2)
    return [f'{c1}.{aa1}{rest1}', f'{c2}.{aa2}{rest2}']


def get_pair_by_ids(pair: List[str], seq: str, joined_ids: Dict[str, int]) -> str:
    b1 = seq[joined_ids[pair[0]]-1]
    b2 = seq[joined_ids[pair[1]]-1]
    return f'{b1}{b2}'


def get_cif_sequence_ids(file: str, label_seq_id:bool=False) -> Tuple[str, Dict[str, int]]:
    """
    This function creates a dictionary of chains, residues and its ids.

    Args:
        file (str): Path to *.cif file
        label_seq_id (bool): Indicates which seq id should be used. By default 'auth_seq_id' is used, however this sometimes raise exception, as some cif files are encoded in a different way. Then the 'label_seq_id' is used.

    Returns:
        Tuple[str, Dict[str, int]]: Sequence, Dictionary where the residue id is a key (e.g. 'A.U7') and value is the position in sequence( e.g. 7).
    """
    with open(file) as f:
        lines = f.readlines()

    header = get_cif_header(lines)

    res_name_field = header['auth_comp_id']
    if not label_seq_id:
        res_id_field = header['auth_seq_id']
        res_asym_field = header['auth_asym_id']
    else:
        res_id_field = header['label_seq_id']
        res_asym_field = header['label_asym_id']

    
    pdb_ins_code_field = header['pdbx_PDB_ins_code']
    seq = []
    jids = {}
    counter = 1
    last_res = ""
    for l in lines:
        if l.strip().startswith("ATOM"):
            fields = l.split()
            residue_name = convert_residues(fields[res_name_field])
            residue_id = fields[res_id_field].strip()
            residue_asym = fields[res_asym_field]
            pdb_ins_code = get_pdb_ins_code(fields[pdb_ins_code_field])
            joined_id = "".join(
                [residue_asym, ".", residue_name, residue_id, pdb_ins_code])

            if joined_id != last_res and residue_name.upper() in ['A', 'C', 'G', 'U']:
                seq.append(residue_name)
                jids[joined_id] = counter
                counter += 1
                last_res = joined_id
    return "".join(seq), jids


def get_pdb_ins_code(field):
    if field != "?":
        return field.strip()
    else:
        return ""
    # f = field.replace("?", ".")
    # return f.strip()


def get_cif_header(lines):
    header = {}
    lines = lines[3:]
    index = 0
    for a in range(len(lines)):
        l = lines[a].strip()

        if l.startswith("ATOM"):
            return header
        elif l.startswith("_atom_site."):
            name = l.replace("_atom_site.", "").strip()
            header[name] = index
            index += 1


def convert_residues(field):
    i = field.replace("DC", "C")
    i = i.replace("DA", "A")
    i = i.replace("DG", "G")
    i = i.replace("DT", "U")
    return i.strip()


def read_csv_lines(path):
    filter_alphabet = 'ABCDEFGHIJKLMNOPRSTUVWQXYZ'
    filter_alphabet = list(filter_alphabet)
    with open(path) as f:
        lines = f.readlines()
    lines = [l.split(";")[0] for l in lines[1:]]
    lines = [l.split(" - ") for l in lines]
    return lines


def get_sequence(path):
    with open(path.replace(".csv", ".fa")) as f:
        lines = f.readlines()
    return lines[1].strip()


def save_bpseq(path, bpseq, seq):
    with open(path, 'w') as f:
        for i in range(1, len(seq)+1):
            for r in bpseq[i]:
                line = str(i)+" "+seq[i-1]+" " + str(r) + '\n'
                f.write(line)


def get_pairing_mode(csv):
    return False if 'noncanonical.csv' in csv else True


if __name__ == "__main__":
    csv = sys.argv[1]
    fasta = sys.argv[2]
    cif = sys.argv[3]
    output_path = sys.argv[4]
    wobble = get_pairing_mode(csv)
    conversion_pipeline(csv, fasta, cif, output_path, wobble=wobble)

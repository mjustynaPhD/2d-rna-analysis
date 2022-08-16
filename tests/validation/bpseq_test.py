import os
import scripts.validation.make_bpseq_from_csv as mb


def test_wobble_remove():
    path = os.path.join(os.getcwd(), "tests/test-data/")
    seq = "gGGCGCCGGUACGCAAGUACGACGGUACGCUCC"
    mol = '1EXY_1_A'
    csv = os.path.join(path, mol, "noncanonical.csv")
    cif = os.path.join(path, mol, f'{mol}.cif')
    fasta = os.path.join(path, mol, f'{mol}.fa')

    sequence, wbbpseq = mb.convert_to_bpseq(
        csv=csv, cif=cif, fasta=fasta, wobble=True)

    _, nwbbpseq = mb.convert_to_bpseq(
        csv=csv, cif=cif, fasta=fasta, wobble=False)

    num_pairings = [True for b in wbbpseq.values() if len(b) <= 1]
    wbpairs = set([f'{seq[i-1]}{seq[j[0]-1]}' for i,
                   j in wbbpseq.items() if len(j) > 0])
    nwbpairs = set([f'{seq[i-1]}{seq[j[0]-1]}' for i,
                    j in nwbbpseq.items() if len(j) > 0])

    wobble = {'GU', 'UG'}
    assert len(wobble.intersection(wbpairs)) > 0
    assert len(wobble.intersection(nwbpairs)) == 0

    assert all(num_pairings)
    assert sequence == seq.upper()
    assert len(wbbpseq) == len(seq)


def test_pairing_mode():
    noncanon = '/0/noncanonical.csv'
    canon = '/0/whole.csv'
    nc_wobble = mb.get_pairing_mode(noncanon)
    cn_wobble = mb.get_pairing_mode(canon)
    assert nc_wobble == False
    assert cn_wobble == True

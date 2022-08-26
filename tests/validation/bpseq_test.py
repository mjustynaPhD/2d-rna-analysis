import os
import scripts.validation.make_bpseq_from_csv as mb

def test_convert():
    csv = "/data/2d-rna/new-cifs/rnapdbee-cifs//6XQE_1_2x/0/noncanonical.csv"
    cif = "/data/2d-rna/new-cifs/cifs//6XQE_1_2x.cif"
    fasta = "/data/2d-rna/new-cifs/fasta500//6XQE_1_2x.fa"
    seq, bpseq = mb.convert_to_bpseq(csv, fasta, cif)
    assert len(seq) > 0

def test_convert2():
    csv = "/data/2d-rna/new-cifs/rnapdbee-cifs/6NUO_1_RB/0/noncanonical.csv"
    cif = "/data/2d-rna/new-cifs/cifs/6NUO_1_RB.cif"
    fasta = "/data/2d-rna/new-cifs/fasta500/6NUO_1_RB.fa"
    seq, bpseq = mb.convert_to_bpseq(csv, fasta, cif)
    assert len(seq) > 0

def test_convert3():
    csv = "/data/2d-rna/new-cifs/rnapdbee-cifs//6O90_1_B/0/noncanonical.csv"
    cif = "/data/2d-rna/new-cifs/cifs//6O90_1_B.cif"
    fasta = "/data/2d-rna/new-cifs/fasta500//6O90_1_B.fa"
    seq, bpseq = mb.convert_to_bpseq(csv, fasta, cif)
    assert len(seq)

def test_convert4():
    csv = "/data/2d-rna/new-cifs/rnapdbee-cifs/6TPQ_1_V/0/noncanonical.csv"
    cif = "/data/2d-rna/new-cifs/cifs/6TPQ_1_V.cif"
    fasta = "/data/2d-rna/new-cifs/fasta500/6TPQ_1_V.fa"
    seq, bpseq = mb.convert_to_bpseq(csv, fasta, cif)
    assert len(seq)

def test_convert5():
    csv = "/data/2d-rna/rnapdbee-cifs/1AKX_1_A/0/noncanonical.csv"
    cif = "/data/2d-rna/cifs/1AKX_1_A.cif"
    fasta = "/data/2d-rna/fasta500/1AKX_1_A.fa"
    seq, bpseq = mb.convert_to_bpseq(csv, fasta, cif)
    assert len(seq)

def test_convert6():
    csv = "/data/2d-rna/rnapdbee-cifs/1DK1_1_B/0/noncanonical.csv"
    cif = "/data/2d-rna/cifs/1DK1_1_B.cif"
    fasta = "/data/2d-rna/fasta500/1DK1_1_B.fa"
    seq, bpseq = mb.convert_to_bpseq(csv, fasta, cif)
    assert len(seq)


def test_get_file():
    path = "/data/2d-rna/new-cifs/cifs/6NUO_1_RB.cif"
    seq, jid = mb.get_cif_sequence_ids(path)
    assert len(seq) == 120
    assert len(jid) == 120

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

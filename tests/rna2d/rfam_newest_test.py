from rna2d.pipelines import RfamNew

RFAM142 = "tests/test-data/rfam142.pdb"
RFAM148 = "tests/test-data/rfam148.pdb"
RESULTS = "tests/test-data/new-results.rpt"


def test_mapping():
    rnew = RfamNew(RESULTS, RFAM142, RFAM148)
    new_mapping = rnew.get_new_mapping()
    assert len(new_mapping) == 1977


def test_newest():
    rnew = RfamNew(RESULTS, RFAM142, RFAM148)
    results, indeces = rnew.get_newest_only()
    assert len(results) == 11
    assert len(indeces) == 11
    assert len(results['spot-rna']) == 989

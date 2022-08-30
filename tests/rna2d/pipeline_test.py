from rna2d.pipelines import Results, BGSURepresentatives

def test_basic_pipeline():
    p = Results("tests/test-data/results.rpt")
    methods, indeces = p.run_for_all()
    for tool in methods:
        assert len(indeces[tool]) >0

def test_filtering():
    p = Results("tests/test-data/results.rpt")
    methods, indeces = p.run_for_all()
    _, filter_i = p.filter_by_molecules(methods, indeces, "tests/test-data/representants.txt")
    for tool in methods:
        assert len(filter_i[tool]) < len(indeces[tool])
        assert len(indeces[tool]) > 0
    
def test_bgsu():
    bgsu = BGSURepresentatives()
    pdbs = bgsu.extract_representatives("tests/test-data/nrlist_3.242_3.0A.csv")
    assert len(pdbs) == 1646

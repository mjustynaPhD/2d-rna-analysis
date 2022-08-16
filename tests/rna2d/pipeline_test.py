from rna2d.pipelines import Pipeline

def test_basic_pipeline():
    p = Pipeline('tests/test-data/tmp/', "tests/test-data/results.rpt")
    methods, indeces = p.run_for_all()
    for tool in methods:
        assert len(indeces[tool]) >0

def test_filtering():
    p = Pipeline('tests/test-data/tmp/', "tests/test-data/results.rpt")
    methods, indeces = p.run_for_all()
    _, filter_i = p.filter_by_molecules(methods, indeces, "tests/test-data/representants.txt")
    for tool in methods:
        assert len(filter_i[tool]) < len(indeces[tool])
        assert len(indeces[tool]) > 0
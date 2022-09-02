from rna2d.pipelines import Results
from rna2d.utils import get_means_stds, get_DataFrames, get_names


def test_get_DataFrame():
    p = Results("tests/test-data/new-results.rpt")
    methods_results, indeces = p.run_for_all()
    means, stds, dfs = get_means_stds(methods_results, indeces, names=True)
    df_means, df_stds = get_DataFrames(means, stds)
    names = sorted(get_names().values())
    assert sorted(means.keys()) == names
    assert sorted(df_means.index) == names

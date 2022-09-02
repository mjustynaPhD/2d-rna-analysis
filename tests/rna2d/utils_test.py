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


def test_get_DataFrame_selected():
    p = Results("tests/test-data/new-results.rpt")
    methods_results, indeces = p.run_for_all()
    sel_methods = ['spot-rna', 'e2efold', 'ipknot', 'ufold']
    means, stds, _ = get_means_stds(
        methods_results,
        indeces,
        names=True,
        selected_methods=sel_methods
    )
    df_means, _ = get_DataFrames(means, stds)

    means_false, stds_false, _ = get_means_stds(
        methods_results,
        indeces,
        names=False,
        selected_methods=sel_methods
    )
    df_means_false, _ = get_DataFrames(means_false, stds_false)
    names_true = sorted([get_names()[n] for n in sel_methods])
    assert sorted(means.keys()) == names_true
    assert sorted(df_means.index) == names_true
    assert len(means.keys()) == 4
    assert len(df_means.index) == 4

    assert sorted(means_false.keys()) == sorted(sel_methods)
    assert sorted(df_means_false.index) == sorted(sel_methods)
    assert len(means_false.keys()) == 4
    assert len(df_means_false.index) == 4

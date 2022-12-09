def get_type_colors():
    """Return color by type of method with the following scheme:
    SL methods - 0
    DL methods - 1
    Traditional - 2

    Return:
    Dict: colors assigned to the method
    """
    colors = {
        'contextFold': 0,
        'contrafold': 0,
        'mxfold': 0,
        'e2efold': 1,
        'mxfold2': 1,
        'rna-state-inf': 1,
        'spot-rna': 1,
        'ufold': 1,
        'ipknot': 2,
        'rnafold': 2,
        'rna-structure': 2
    }
    return colors
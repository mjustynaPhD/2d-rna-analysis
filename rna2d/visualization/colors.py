def get_type_colors():
    """Return color by type of method with the following scheme:
    SL methods - 0
    DL methods - 1
    Traditional - 2

    Return:
    Dict: colors assigned to the method
    """
    colors = {
        'contextFold': 1,
        'contrafold': 1,
        'mxfold': 1,
        'e2efold': 0,
        'mxfold2': 0,
        'rna-state-inf': 0,
        'spot-rna': 0,
        'spot-rna2': 0,
        'ufold': 0,
        'ipknot': 2,
        'rnafold': 2,
        'rnaalifold': 2,
        'rna-structure': 2,
        'rscape':2,
    }
    return colors
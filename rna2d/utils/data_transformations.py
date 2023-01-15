from typing import List
import numpy as np
import pandas as pd


def get_sns_data(dfs, df_means, names:dict, order:list = None, colors_dict:dict = {}) -> pd.DataFrame:
    mcc_dfs = {}
    if order is None:
        order = sorted(dfs.keys())
    for m in order:
        mcc_df = pd.DataFrame(dfs[m]['INF'])
        mcc_df.rename(columns={"INF": m}, inplace=True)
        mcc_dfs[m] = mcc_df

    all_dfs = list(mcc_dfs.values())
    x = all_dfs[0].join(all_dfs[1:])

    m = []
    inf = []
    means:List[float] = []
    colors = []
    if order is None:
        order = df_means.index
    
    for met in order:
        inf.extend(x[met].values)
        m.extend(np.full(len(x[met].values), names[met]))
        means.extend(np.full(len(x[met].values), str(round(x[met].mean(), 2))))
        colors.extend(np.full(len(x[met].values), colors_dict.get(met, 0)))
    sns_df = pd.DataFrame({"Method": m, "INF": inf, 'Means': means, 'Color': colors})
    return sns_df

import os
from typing import Any, Dict, List, Tuple
import pandas as pd

NAMES = {
    'spot-rna': 'SPOT-RNA',
    'mxfold2': 'MXfold2',
    'ufold': 'UFold',
    'contextFold': 'Contextfold',
    'ipknot': 'IPknot',
    'contrafold': 'CONTRAfold',
    'rnafold': 'RNAFold',
    'mxfold': 'MXfold',
    'rna-state-inf': 'RNA State Inf.',
    'rna-structure': 'RNAStructure',
    'e2efold': 'E2efold'
    }


def get_pdb_ids(path):
    pdbs = os.listdir(path)
    pdbs = [p.replace("-", "_") for p in pdbs]
    pdbs = [f'{p[:4].upper()}{p[4:]}' for p in pdbs]
    pdbs = [f'{p.split("_")[0]}_{p.split("_")[2]}' for p in pdbs]
    return pdbs


def get_names() -> Dict[str, str]:
    return NAMES


def get_results(res_path):
    with open(res_path) as f:
        results = f.readlines()
    return results


def get_subset_ids(results):
    subset_ids = {}
    k = ""
    counter = 0
    for line in results:
        l = line.split()
        if len(l) == 0:
            break
        elif len(l) == 1:
            k = l[0]
        elif l[0] != "Tool":
            method = l[0]
            res = l[1:]
            res = [float(r) for r in res]
            if method not in subset_ids:
                subset_ids[method] = []
            subset_ids[method].append(k)
        counter += 1
    return subset_ids


def filter_common(subset_ids, keys: list = None):
    sets = []
    if keys is None:
        keys = list(subset_ids.keys())
    for m in keys:
        sets.append(set(subset_ids[m]))
    common = sets[0].intersection(*sets)
    return common


def collect_results(results, common, subset_ids):
    pdb_id_res = {}
    k = ""
    for l in results:
        l = l.split()
        if len(l) == 0:
            pass
        elif len(l) == 1:
            k = l[0]
            if k in common:
                pdb_id_res[k] = {}
        elif l[0] != "Tool":
            method = l[0]
            res = l[1:]
            res = [float(r) for r in res]
            if k in common:
                pdb_id_res[k][method] = res
    return join_results(subset_ids, pdb_id_res)


def join_results(subset_ids, pdb_id_res):
    met_res = {}
    indeces = {}
    for method in subset_ids.keys():
        # for method in ['spot-rna', 'e2efold', 'ipknot', 'ufold']: # for pseudoknots
        if method not in met_res:
            met_res[method] = []
            indeces[method] = []
        for k_id in pdb_id_res.keys():
            if method not in pdb_id_res[k_id]:
                print(
                    f"Results missing for method: {method} for molecule: {k_id}")
                continue
            met_res[method].append(pdb_id_res[k_id][method])
            indeces[method].append(k_id)
    return met_res, indeces


def get_means_stds(
    met_res,
    indeces,
    out_path: str = None,
    cols: list = ['PPV', 'TPR', 'F1', 'INF'],
    names: bool = False
) -> Tuple[Dict[Any, Any], Dict[Any, Any], Dict[Any, Any]]:
    dfs = {}
    means = {}
    stds = {}
    for name, vals in met_res.items():
        if names:
            tag_name = get_names()[name]
        else:
            tag_name = name
        df = pd.DataFrame(vals, columns=cols, index=indeces[name])
        if out_path is not None:
            os.makedirs(out_path, exist_ok=True)
            df.to_csv(os.path.join(out_path, name+".csv"))
        dfs[tag_name] = df
        res = df.mean().to_list()
        res = [round(r, 2) for r in res]
        res_std = df.std().to_list()
        res_std = [round(r, 2) for r in res_std]
        means[tag_name] = res
        stds[tag_name] = res_std
    return means, stds, dfs


def get_DataFrames(
    means, stds,
    out_path: str = None,
    name: str = "all",
    cols: List[str] = ['PPV', 'TPR', 'F1', 'INF']
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_means = pd.DataFrame(means.values(), columns=cols, index=means.keys())
    df_means = df_means.sort_values("INF", ascending=False)

    df_std = pd.DataFrame(stds.values(), columns=cols, index=df_means.index)
    # df_std = df_std.sort_values(df_means['INF-MCC'], ascending=False)
    if out_path is not None:
        os.makedirs(out_path, exist_ok=True)
        df_means.to_csv(os.path.join(out_path, name+"-means.csv"))
        df_std.to_csv(os.path.join(out_path, name+"-stds.csv"))
    return df_means, df_std

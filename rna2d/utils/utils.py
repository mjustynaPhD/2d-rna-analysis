import os
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd

NAMES = {
    'spot-rna': 'SPOT-RNA',
    'mxfold2': 'MXfold2',
    'spot-rna2': "SPOT-RNA2",
    'ufold': 'UFold',
    'contextFold': 'Contextfold',
    'ipknot': 'IPknot',
    'contrafold': 'CONTRAfold',
    'rnafold': 'RNAFold',
    'mxfold': 'MXfold',
    'rna-state-inf': 'RNA-state-inf',
    'rna-structure': 'RNAStructure',
    'e2efold': 'E2efold',
    'rnaalifold': 'RNAalifold',
    'rscape': 'R-scape',
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


def get_subset_ids(results, ignored_methods: list = []):
    subset_ids = {}
    k = ""
    counter = 0
    for lineine in results:
        l = lineine.split()
        if len(l) == 0:
            break
        elif len(l) == 1:
            k = l[0]
        elif l[0] != "Tool":
            method = l[0]
            res = l[1:]
            res = [float(r) for r in res]
            if method not in subset_ids and method not in ignored_methods:
                subset_ids[method] = []
            elif method not in ignored_methods:
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
                    f"Results missing for method: {method} for molecule:\
                        {k_id}"
                )
                continue
            met_res[method].append(pdb_id_res[k_id][method])
            indeces[method].append(k_id)
    return met_res, indeces


def get_means_stds(
    met_res,
    indeces,
    out_path: str = None,
    cols: list = ['PPV', 'TPR', 'F1', 'INF'],
    names: bool = False,
    selected_methods: List[str] = None
) -> Tuple[Dict[Any, Any], Dict[Any, Any], Dict[Any, Any]]:
    dfs = {}
    means = {}
    stds = {}
    if selected_methods is None:
        selected_methods = met_res.keys()
    for name, vals in met_res.items():
        if names:
            tag_name = get_names()[name]
        else:
            tag_name = name
        if name not in selected_methods and tag_name not in selected_methods:
            continue
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

    df_std = pd.DataFrame(stds.values(), columns=cols, index=df_means.index)
    if out_path is not None:
        os.makedirs(out_path, exist_ok=True)
        df_means.to_csv(os.path.join(out_path, name+"-means.csv"))
        df_std.to_csv(os.path.join(out_path, name+"-stds.csv"))
    return df_means, df_std


def get_single_representative(
        all_indeces:list,
        pk_indeces:list,
        novel_keys:list,
        mapping:dict,
        seed:int=0
    ) -> list:
    """Generate a single random representative for each family.

    Args:
        all_indeces (list): List of PDB ids for type all.
        pk_indeces (list): List of PDB ids for type pseudoknot.
        novel_keys (list): List of novel families ids.
        mapping (dict): Mapping of PDB ids to family ids.
        seed (int, optional): Seed for random state. Defaults to 0.

    Returns:
        list: list of PDB ids considered as representatives.
    """
    np.random.seed(seed)
    l = {}
    np.random.shuffle(pk_indeces)
    for i in pk_indeces:
        v =  mapping.get(i, 0)
        if v not in l and i in novel_keys:
            l[v] = i

    np.random.shuffle(all_indeces)
    for i in all_indeces:
        v =  mapping.get(i, 0)
        
        if v not in l and i in novel_keys:
            l[v] = i
    return list(l.values())
    # return l
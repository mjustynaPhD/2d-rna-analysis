from dataclasses import dataclass
from typing import Dict, List, Tuple
import pandas as pd
from rna2d.pipelines import Results
from rna2d.utils import get_means_stds
from rna2d.utils import get_sns_data, get_names, get_DataFrames


@dataclass
class SeabornData():
    results: Tuple[Dict[str, List[float]]]
    indeces: Dict[str, List[str]]

    def get_sns_format_data(self, names: Dict[str, str] = None, order: list = None, colors_dict: dict = {}) -> pd.DataFrame:
        if names is None:
            names = get_names()
        means, stds, dfs = get_means_stds(self.results, self.indeces)
        means_df, _ = get_DataFrames(means, stds)
        return get_sns_data(dfs, means_df, names, order=order, colors_dict=colors_dict)

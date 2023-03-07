
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple, Union
import pandas as pd

from rna2d.utils import (get_results, get_subset_ids,
                         filter_common, collect_results)


@dataclass
class Results():
    results_path: str
    ignored_methods: List[str] = None

    def run_for_all(self) -> Tuple[Dict[str, List[float]],
                                   Dict[str, List[str]]]:
        res = get_results(res_path=self.results_path)
        ids = get_subset_ids(res, ignored_methods=self.ignored_methods)
        common = filter_common(ids)
        methods_results, indeces = collect_results(res, common, ids)
        return methods_results, indeces

    def filter_by_molecules(
        self,
        methods_results: Dict[str, List[float]],
        indeces: Dict[str, List[str]],
        filtering: Union[str, Path]
    ) -> Tuple[Dict, Dict]:
        """Filters results by list of molecules indicated in file.

        Args:
            methods_results (Dict[str, List[float]]): Results of each method.
            indeces (Dict[str, List[str]]): Indeces for each method.
            filtering (Union[str, Path]): Path to file with ids to filter out.

        Returns:
            Tuple[Dict, Dict]: Updated results and indeces with
                removed indeces from file.
        """
        with open(filtering) as f:
            repres = f.readlines()
        repres = [r.strip() for r in repres]
        # Remove doule stranded molecules
        repres = [r for r in repres if '-' not in r]

        new_methods: Dict[str, List] = {}
        new_indeces: Dict[str, List] = {}
        for tool in methods_results:
            common_ind = set(indeces[tool])
            common_ind = list(common_ind.intersection(repres))
            df = pd.DataFrame(methods_results[tool], columns=[
                            'PPV', 'TPR', 'F1', 'INF'], index=indeces[tool])
            res = df.loc[common_ind]
            new_methods[tool] = res.values
            new_indeces[tool] = res.index.tolist()

        return new_methods, new_indeces

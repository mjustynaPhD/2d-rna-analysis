from dataclasses import dataclass
from typing import Dict, Tuple
from rna2d.utils import *


@dataclass
class Pipeline():
    out_path: str
    results_path: str

    def run_for_all(self) -> Tuple[Dict, Dict]:
        res = get_results(out_path=self.out_path, res_path=self.results_path)
        ids = get_subset_ids(res)
        common = filter_common(ids)
        methods_results, indeces = collect_results(res, common, ids)
        return methods_results, indeces

    def run_filtered(self, filter_ids_path: str):
        methods_results, indeces = self.run_for_all()

        pass

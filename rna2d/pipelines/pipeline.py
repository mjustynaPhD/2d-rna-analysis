from rna2d.utils import *

class Pipeline():
    def __init__(self, *args, **kwargs):
        pass

    def run_for_all(self, out_path:str, results_path:str):
        res = get_results(out_path=out_path, res_path=results_path)
        ids = get_subset_ids(res)
        common = filter_common(ids)        
        methods_results, indeces = collect_results(res, common, ids)
        return methods_results, indeces

    def run_filtered(self):
        pass
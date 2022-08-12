from rna2d.utils import get_results, get_subset_ids

class Pipeline():
    def __init__(self, *args, **kwargs):
        pass

    def run_for_all(self):
        res_all = get_results('all', "/data/2d-rna/validation-all-non0/results.rpt")
        res_wc = get_results('canon', "/data/2d-rna/validation-canon-non0/results.rpt")
        res_nwc = get_results('noncanon', "/data/2d-rna/validation-noncanon-non0/results.rpt")
        res_pk = get_results('pseudoknots', "/data/2d-rna/validation-pseudoknots/results.rpt")



    def run_filtered(self):
        pass
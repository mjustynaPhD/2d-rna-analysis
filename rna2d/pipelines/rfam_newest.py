from dataclasses import dataclass
from typing import Dict, List
import pandas as pd
from rna2d.pipelines import Results
from rna2d.utils import Rfam, get_names


@dataclass
class RfamNew():
    results_path: str
    rfam_old: str
    rfam_new: str
    tool: str = "spot-rna"

    def get_newest_only(self, filter: List[str] = None):
        p = Results(self.results_path)
        methods, indeces = p.run_for_all()
        converted_indeces = [
            f'{p.split("_")[0]}_{p.split("_")[2]}' for p in indeces[self.tool]]
        new_mapping = self.get_new_mapping()
        if filter is not None:
            rfam = Rfam()
            new_mapping = rfam.filter_out_list(filter, new_mapping)
        common_ind = set(converted_indeces)
        common_ind = list(common_ind.intersection(set(new_mapping.keys())))
        res = {}
        conv_ind = {}
        for k in get_names():
            converted_indeces = [
                f'{p.split("_")[0]}_{p.split("_")[2]}' for p in indeces[k]]
            df = pd.DataFrame(methods[k], columns=[
                'PPV', 'TPR', 'F1', 'INF'], index=converted_indeces)
            conv_ind[k] = converted_indeces
            res[k] = df.loc[common_ind]
        return res, conv_ind

    def get_new_mapping(self) -> Dict[str, str]:
        """Returns mapping of PDB ids on RFam families.
        E.g.,
        {'6ZYM_5': 'RF00020',
        ...
        }

        Returns:
            Dict[str, str] : Mapping of PDB ids on RFam families ids.
        """
        rfam = Rfam()
        rfamO_mapping = rfam.get_pdb_family_mapping(self.rfam_old)
        rfamN_mapping = rfam.get_pdb_family_mapping(self.rfam_new)
        new_mapping = rfam.get_new_keys_only(rfamO_mapping, rfamN_mapping)
        return new_mapping

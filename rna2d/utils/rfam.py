from dataclasses import dataclass
from typing import Dict

@dataclass
class Rfam():

    def get_pdb_family_mapping(self, rfam_pdb_path:str)->Dict[str, str]:
        with open(rfam_pdb_path) as f:
            lines = f.readlines()
        pdb_mapping = [l.strip() for l in lines]
        pdb_mapping = [l.split('\t') for l in pdb_mapping]

        pdbs_families = {}
        for p in pdb_mapping[1:]:
            family = p[0]
            pdb_id = p[1]
            chain = p[2]
            full_id = f'{pdb_id.upper()}_{chain}'
            pdbs_families[full_id] = family
        return pdbs_families

    def get_new_keys_only(self, old:Dict[str,str], new:Dict[str,str])->Dict[str, str]:
        old_keys = set(old.keys())
        new_keys = set(new.keys())
        key_difference = new_keys.difference(old_keys)
        
        new_dict = {}
        for k in key_difference:
            if k in new:
                new_dict[k] = new[k]
            else:
                print(k)
        return new_dict
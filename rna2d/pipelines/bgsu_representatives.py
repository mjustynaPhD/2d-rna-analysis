
from os import PathLike
from typing import List, Union


class BGSURepresentatives():
    
    def extract_representatives(self, path:Union[str, PathLike]) -> List:
        with open(path) as f:
            lines = f.readlines()
        pdbs = [l.strip() for l in lines]
        pdbs = [p.split(',')[1:2] for p in pdbs]
        pdbs = [self._combine_ids(p) for p in pdbs]
        pdbs = [p[0] for p in pdbs]
        # pdb_repres = [f'{p.split("_")[0]}_{p.split("_")[2]}' for p in pdbs]
        return pdbs

    def _additional_chains(self, pdb:str) -> str:
        """Join pdb id if it contain additional chain.

        Args:
            pdb (str): PDB entry from bgsu list.

        Returns:
            str: Returns PDB id joined with "-", e.g. <1ABC>_1_A-B if it contains additional chain.
        """
        if '+' in pdb:
            pdb_split = pdb.split("+")
            pdb_ab = [p.split("|") for p in pdb_split]
            core = "_".join(pdb_ab[0][:-1])
            pdb = f"{core}_{pdb_ab[0][-1]}-{pdb_ab[1][-1]}"
        else:
            pdbl = pdb.split("|")
            pdb = "_".join(pdbl)
        return pdb

    def _combine_ids(self, pdb_line:str) -> List[str]:
        """Creates list of PDB id from a given line

        Args:
            pdb_line (str): Line with PDB ids from BGSU txt file

        Returns:
            List[str]: List of PDB ids.
        """
        pdbs = [p.replace("\"", "").replace("\'", "") for p in pdb_line]
        pdbs = [self._additional_chains(p) for p in pdbs]
        return pdbs
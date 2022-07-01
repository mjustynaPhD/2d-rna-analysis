#! /usr/bin/env python
import sys

from pdbx import PdbxReader, PdbxWriter


def override_auth_with_label(container, categories):
    for row in container.row_list:
        for category in categories:
            try:
                label_index = container.attribute_list.index(f'label_{category}_id')
                auth_index = container.attribute_list.index(f'auth_{category}_id')
                if row[label_index]:
                    row[auth_index] = row[label_index]
            except ValueError:
                # if some category is not found, just ignore it
                continue


if __name__ == '__main__':
    data = []
    reader = PdbxReader(sys.stdin)
    reader.read(data)

    if data:
        atom_site = data[0].get_object('atom_site')
        unobs = data[0].get_object('pdbx_unobs_or_zero_occ_residues')

        if atom_site:
            override_auth_with_label(atom_site, ['asym', 'atom', 'comp', 'seq'])

        if unobs:
            override_auth_with_label(unobs, ['asym', 'comp', 'seq'])

        writer = PdbxWriter()
        writer.write(data)

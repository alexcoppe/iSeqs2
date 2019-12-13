#!/usr/bin/env python

import argparse
import os.path
import sys
import zipfile

def build_thpa_dictionary(normal_tissue_file_path, cell_types = ["B-cells", "NK-cells", "T-cells", "bone marrow", "dendritic cells", "granulocytes", "monocytes"], min_nx = 1):
    d = {}
    zfile = zipfile.ZipFile(normal_tissue_file_path)
    cell_types = set(cell_types)
    for finfo in zfile.infolist():
        if finfo.filename == 'rna_tissue_consensus.tsv':
            ifile = zfile.open(finfo)
            line_list = ifile.readlines()
            for line in line_list:
                line = str(line).replace("\\t", "\t")
                splitted_line = line.split("\t")
                tissue = splitted_line[2]
                nx = splitted_line[3]
                try:
                    nx = float(nx[:-3])
                except:
                    continue
                if tissue in cell_types and nx >= min_nx:
                    if not (splitted_line[1] in d):
                        d[splitted_line[1]] = [splitted_line[2]]
                    else:
                        d[splitted_line[1]].append(splitted_line[2])
    return(d)
    


def main():
    parser = argparse.ArgumentParser(description="Filter by rna_tissue_consensus.tsv.zip consensus transcript expression levels")
    parser.add_argument('-n', '--normal_tissue', action='store', type=str, help="rna_tissue_consensus.tsv.zip file path", required=False, default=None)
    args = parser.parse_args()

    normal_tissue = args.normal_tissue

    thpa_dictionary = build_thpa_dictionary(normal_tissue)
    for key in thpa_dictionary.keys():
        print(thpa_dictionary.get(key))

    
if  __name__ == "__main__":
    main()


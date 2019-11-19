# build_leukemia_genes_list.py

This scripts creates a text file containing the genes from [Cancer Genome Census](https://cancer.sanger.ac.uk/census) and [Leukemia Gene Literature Database (dbLGL)](http://soft.bioinfo-minzhao.org/lgl/).

### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None
| -l | --lgld | The flat file from human cancer leukemia genes | File path | None |
| -C | --cosmic | The flat file from COSMIC's Cancer Gene Census (CGC) | File path | None |

### Usage

```
build_leukemia_genes_list.py -l dbs/dbLGL_human.txt -c dbs/cancer_gene_census.csv
```

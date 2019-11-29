# filter_vcf_by_gene_names.py

This script filters a VCF file by **names** of genes. 
The list of genes to be retained or removed (--throw option set to T) should be in a file with one **gene name** by line, like the one produced by
[build_leukemia_genes_list.py script](https://github.com/alexcoppe/iSeqs2/blob/master/scripts/build_leukemia_genes_list/README.md).

### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None
| -g | --genes | A file with one gene name per line | File path | None |
| -v | --vcf | The VCF to be filtered | File path | None |
| -m | --meta | Show or not show meta-information of the VCF | T or F | T |
| -t | --throw | Throw away genes present in the file indicated by -g | T or F | F |

### Usage

Retain genes from genes_file.txt file:

```
filter_vcf_by_gene_names.py -g genes_file.txt -v vcf_to_be_filtered.vcf
```

Remove genes from genes_file.txt file:

```
filter_vcf_by_gene_names.py -g genes_file.txt -v vcf_to_be_filtered.vcf -t T
```

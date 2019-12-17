# filter_by_normal_expression.py

A script that filters a VCF using RNA consensus tissue gene data obtained from [https://www.proteinatlas.org](https://www.proteinatlas.org/about/download).
The **NX** column is used as level of expression to be filtered, use the -x parameter to change it. Default value is 1 meaning that only genes with **NX >= 1** will pass the filter.

To download the data go to [www.proteinatlas.org/about/download](https://www.proteinatlas.org/about/download) and get the rna_tissue_consensus.tsv.zip file.

### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None |
| -n | --normal_tissue | The location of the rna_tissue_consensus.tsv.zip file | PATH | None | 
| -v | --vcf | The location of the VCF to be filtered | PATH | None |
| -x | --nx | The minimum value of NX to be used for filtered | Integer | 1 |

### Usage

```
filter_by_normal_expression.py -n  rna_tissue_consensus.tsv.zip  -v vcf_to_be_filtered.vcf -x 2
```

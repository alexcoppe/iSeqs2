# remove_snps_from_cosmic.py

This script filters out the **SNPs** from a VCF using [COSMIC](https://cancer.sanger.ac.uk/cosmic) annotation. 
It is usefull because SnpSift is buggy and some times
 adds a **";SNP;" sub-field** in the INFO column.
It uses the VCF of coding or non-coding mutations from [COSMIC](https://cancer.sanger.ac.uk/cosmic) usually called 
CosmicCodingMuts.vcf.gz and only non-academic organisations need to pay a license fee to obtain it. 


### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None
| -c | --cosmic | The file path of the Cosmic file | File path | None |
| -v | --vcf | The VCF to be filtered by SNPs from COSMIC | File path | None |


### Usage

```
remove_snps_from_cosmic.py -v vcf_with_SNPs_to_be_removed.vcf -c CosmicCodingMuts.vcf.gz
```

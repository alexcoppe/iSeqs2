# iSeqs2
Another bunch of scripts I use in my Next Generation Sequencing Bioinformatics Analyses

## Scripts available

| Script | Description |
| ------------- |:-------------|
|[build_leukemia_genes_list.py](https://github.com/alexcoppe/iSeqs2/blob/master/scripts/build_leukemia_genes_list/README.md) | Creates a text file containing the genes from [Cancer Genome Census](https://cancer.sanger.ac.uk/census) and [Leukemia Gene Literature Database (dbLGL)](http://soft.bioinfo-minzhao.org/lgl/)|
| [filter_by_normal_expression.py](https://github.com/alexcoppe/iSeqs2/tree/master/scripts/filter_by_normal_expression) | Filters a VCF using RNA consensus tissue gene data obtained from [https://www.proteinatlas.org](https://www.proteinatlas.org/about/download). The **NX** column is used as level of expression to be filtered |
|[filter_strelka2.py](https://github.com/alexcoppe/iSeqs2/tree/master/scripts/filter_strelka2)|Given a VCF produced by [Strelka2](https://github.com/Illumina/strelka) variant caller filters it by the **SDP / DP**, **QSS_NT** and **FDP**|
|[filter_vcf_by_gene_names.py](https://github.com/alexcoppe/iSeqs2/tree/master/scripts/filter_vcf_by_gene_names/README.md)|A script that filters a VCF based on a list of genes from another file like the one generated by [build_leukemia_genes_list.py](https://github.com/alexcoppe/iSeqs2/blob/master/scripts/build_leukemia_genes_list/README.md) script|
|[remove_snps_from_cosmic.py](https://github.com/alexcoppe/iSeqs2/tree/master/scripts/remove_snps_from_cosmic)| Filter out the SNPs from a VCF using [COSMIC](https://cancer.sanger.ac.uk/cosmic) annotation. It is usefull because [SnpSift](http://snpeff.sourceforge.net/SnpSift.html) is buggy and some times adds a ";SNP;" sub-field in the INFO column. It needs the VCF of coding or non-coding mutations from COSMIC usually called CosmicCodingMuts.vcf.gz|

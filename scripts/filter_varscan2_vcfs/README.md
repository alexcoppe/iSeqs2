# filter_varscan2_vcfs.py

This scripts filters somatic variants from a VCFs produced by [VarScan2](http://varscan.sourceforge.net/) using the somaticFilter command from VarScan.
To obtain a VCF you need to [vs_format_converter.py](https://github.com/alexcoppe/varscan_accessories) 
script from the [varscan_accessories](https://github.com/alexcoppe/varscan_accessories).

```
python ~/bin/vs_format_converter.py varscan_snp_filtered.snp > varscan_snp_filtered.vcf
```

### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None |
| -c | --min_coverage| Minimum read depth | Int | 20 |
| -r | --min_reads2 | Minimum supporting reads for a variant | Int | 5 |
| -s | --min_strands2 | Minimum # of strands on which variant observed | Int | 1 |
| -q | --min_avg_qual | Minimum average base quality for variant-supporting reads | Int | 30 |
| -f | --min_coverage | Minimum variant allele frequency threshold | Float | 0.05 |
| -p | --p_value | Default p-value threshold for calling variants | Float | 0.05 |
| -d | --directory | The directory containing VarScan2 VCFs | Str | . |
| -o | --output_directory | The output directory | Str | . |

### Usage example

```
filter_varscan2_vcfs.py -c 10 -r 5 -s 2 -q 20 -f 0.05 -p 0.03 -d ./CK_RICADUTAST_CK_CONTROLLO -O ~/VarScan2
```

The above comand will launch the following one on all Varscan2 VCFs found in the ./CK_RICADUTAST_CK_CONTROLLO directory.

```
java -jar ~/local/varscan.jar somaticFilter ./CK_RICADUTAST_CK_CONTROLLO/06_varscan_snp_cosmic.vcf --output-file ~/VarScan2/CK_RICADUTAST_CK_CONTROLLO_varscan.vcf --min-coverage 10 --min-reads2 5 --min-strands21 --min-avg-qual 20 --min-var-freq 0.05 --p-value 0.03
```

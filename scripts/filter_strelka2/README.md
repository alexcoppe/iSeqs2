# filter_strelka2_by_sdp.py

Given a VCF produced by [Strelka2](https://github.com/Illumina/strelka) variant caller filters it by the **SDP / DP**.

- **SDP**: number of reads with deletions spanning this site at tier1
- **DP**: read depth for tier1 (used+filtered)


### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None
| -v | --vcf | The flat file from human cancer leukemia genes | File path | None |
| -r | --ratio | The ration between SDP and DP should be smaller than -r varlue | Float | 0.75 |

### Usage

```
filter_strelka2_by_sdp.py  -v 08_strelka2_snvs_gt.vcf -r 0.7
```

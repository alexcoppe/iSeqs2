# filter_strelka2_by_sdp.py

Given a VCF produced by [Strelka2](https://github.com/Illumina/strelka) variant caller filters it by **SDP / DP**, **QSS_NT**, and **FDP**.

- **SDP**: number of reads with deletions spanning this site at tier1
- **DP**: read depth for tier1 (used+filtered)
- **QSS_NT**: Quality score reflecting the joint probability of a somatic variant and NT
- **FDP**:  Number of basecalls filtered from original read depth for tier1 


### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None
| -v | --vcf | The flat file from human cancer leukemia genes | File path | None |
| -q | --qss_nt | Quality score reflecting the joint probability of a somatic variant and NT | Int | 15 |
| -f | --fdp | Number of basecalls filtered from original read depth for tier1 | Int | 4 |
| -r | --ratio | The ration between SDP and DP should be smaller than -r varlue | Float | 0.75 |

### Usage

```
filter_strelka2_by_sdp.py  -v 08_strelka2_snvs_gt.vcf -r 0.8 -q 16  -f 5 -v VCF_MADE_BY_STRELKA2.vcf
```

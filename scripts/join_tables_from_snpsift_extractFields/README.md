# join_tables_from_snpsift_extractFields.py

Merge the tab separated .txt files created by SnpSift extractFields command.

### Parameters

| Short command line option | Long command line option | Description | Type of parameter | Default |
| ------------- |:-------------| :-------------| :-------------| :-------------|
| -h | --help | Show the help message and exit | None | None
| -d | --directory | The directory containing all the files to be joined | Dir path | None |

### Usage

```
join_tables_from_snpsift_extractFields.py -d 13_tables > merged.txt
```

### Bugs

Still not working with Strelka2 indels VCF

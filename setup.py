import setuptools


#scripts=['change_set_subfield'] ,

setuptools.setup(
     name='iSeqs2',  
     version='0.0.1',
     author="Alessandro Coppe",
     author_email="",
     description="Another bunch of scripts I use in my Next Generation Sequencing Bioinformatics Analyses",
     url="https://github.com/alexcoppe/iSeqs2",
     packages=["iseqs2"],
     scripts=["scripts/build_leukemia_genes_list/build_leukemia_genes_list.py",
         "scripts/filter_strelka2_by_sdp/filter_strelka2_by_sdp.py",
         "scripts/remove_snps_from_cosmic/remove_snps_from_cosmic.py",
         "scripts/filter_vcf_by_gene_names/filter_vcf_by_gene_names.py"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)

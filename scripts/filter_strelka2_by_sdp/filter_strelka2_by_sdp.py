#!/usr/bin/env python

import argparse
import os.path
import sys

def main():
    parser = argparse.ArgumentParser(description="Filter Strelka2 VCF by SDP / DP")
    parser.add_argument('-r', '--ratio', action='store', type=float, help="The ration between SDP and DP should be smaller than -r varlue (default = 0.75)", required=False, default=0.75)
    parser.add_argument('-v', '--vcf', action='store', type=str, help="The vcf to be filtered")
    args = parser.parse_args()
    args = parser.parse_args()

    vcf = args.vcf

    is_a_strelka_vcf = False


    # Check if args.vcf is a strelka VCF file
    with open(vcf) as vcf_content:
        for line in vcf_content.readlines():
            if line.startswith("#"):
                if line.startswith("##content=strelka"):
                    is_a_strelka_vcf = True
                    break

        if is_a_strelka_vcf == False:
            sys.exit("Not a strelka VCF")

    vcf_content.close()


    ################### Do the job ##################

    with open(vcf) as vcf_content:
        for line in vcf_content.readlines():
            if line.startswith("#"):
                print(line[:-1])
            else:
                splitted_line = line.split()
                splitted_format = splitted_line[10].split(":")
                dp = splitted_format[3]
                sdp = splitted_format[6]
                ratio = float(sdp) / float(dp)
                if ratio != 0:
                    print(line[:-1])
 

if  __name__ == "__main__":
    main()

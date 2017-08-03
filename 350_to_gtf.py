#!/usr/bin/python
#usage: python 350_to_gtf.py 350 > output

import sys
for line in open(sys.argv[1],'r'):
    if not (line[:1] == ">"):
        continue
    spl = line[1:].strip().split('_')
    le = len(spl)
    ids = line[1:].strip()
    start = spl[le - 3]
    end = spl[le - 2]
    strand = spl[le - 1]
    ori_id = spl[0]+"_"+spl[1]
    att = "gene_id \""+ids+"\";"
    result = [ori_id,"coding_region","exon",start,end,".",strand,".",att]
    print "\t".join(result)

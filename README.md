# mapping_tools
## get count table from idxstats
```
python get_count_table.py *.idxstat.txt > count.txt
```
## get count table from htseq
```
python get_count_table_from_htseq.py *.count.txt > count.txt
```
## get count from selected location
Arguments: start location, end location, multiple_pileup_files
```
python get_partial_count_from_pileup.py 3318816 3318835 *.pileup > selected.count.txt
```

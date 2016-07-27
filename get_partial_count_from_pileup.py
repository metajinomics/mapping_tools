#this scipt helps to get count of selected area
#usage: python get_partial_count_from_pilup.py 1 100 filename.pileup

import sys
start = int(sys.argv[1])
end = int(sys.argv[2])
#make dictionary
dict = {}
for i in range(start,end+1):
    dict[i]=[]
files = []
for file in sys.argv[3:]:
    files.append(file)
    for line in open(file,'r'):
        spl = line.strip().split('\t')
        loc = int(spl[1])
        if (loc >= start and loc <= end):
            temp = dict[loc]
            temp.append(spl[3])
            dict[loc]=temp

print 'loc\t'+'\t'.join(files)
for item in dict.items():
    print str(item[0])+'\t'+'\t'.join(item[1])

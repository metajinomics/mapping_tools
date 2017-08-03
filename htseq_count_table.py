#!/usr/bin/python

import sys

def main():
    list_id = []
    count = {}
    for n, filename in enumerate(sys.argv[1:]):
        for line in open(filename,'r'):
            if line[:2] == "__":
                continue
            spl = line.strip().split('\t')
            
            if n == 0:
                list_id.append(spl[0])
            if count.has_key(spl[0]):
                temp = count[spl[0]]
                temp.append(spl[1])
                count[spl[0]] = temp
            else:
                count[spl[0]] = [spl[1]]
    #print count
    file = ["gene"]
    for filename in sys.argv[1:]:
        file.append(filename)
    print '\t'.join(file)
    for ids in list_id:
        result = count[ids]
        result.insert(0,ids)
        print '\t'.join(result)


if __name__ == '__main__':
    main()

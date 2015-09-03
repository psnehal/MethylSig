import argparse
import subprocess
import sys
import re
import logging

import numpy
import pysam
parser = argparse.ArgumentParser()
parser.add_argument('--o', action='append', dest='collection1',
                    default=[],
                    help='Add repeated values to a list',
                    )
parser.add_argument('--i', action='append', dest='collection2',
                    default=[],
                    help='Add repeated values to a list',
                    )
parser.add_argument('--c', action='append', dest='collection3',
                    default=[],
                    help='Add repeated values to a list',
                    )
parser.add_argument('--expName', type=str , dest='collection5',
                    help='expName',
                    )
parser.add_argument('--format', type=str , dest='collection6',
                    help='Add format values to a list',
                    )
parser.add_argument('--peakType', type=str , dest='collection7',
                    help='Add peakType values to a list',
                    )
parser.add_argument('--thresh', type=str , dest='collection8',
                    help='Add thresh values to a list',
                    )
parser.add_argument('--removeArt', type=str , dest='collection9',
                    help='Add removeArt values to a list',
                    )
parser.add_argument('--rd_dup', type=str , dest='collection10',
                    help='Add rd_dup values to a list',
                    )	   
results = parser.parse_args()
import subprocess
print 'input file     =', results.collection2
print 'Chip_value   =', results.collection3
print 'expName_switch   =', results.collection5
print 'format       =', results.collection6
print 'peaktype     =', results.collection7
print 'thers   =', results.collection8
print 'removeArt   =', results.collection9
print 'rd_dupt       =', results.collection10


command = "/usr/lib/python2.6/site-packages/PePr/PePr.py -i "
command+=  ', '.join(results.collection2)
command+= " -c "
command+=  ', '.join(results.collection3)
command+=" -n "
command+= results.collection5 
command+= " -f "
command+= results.collection6
command+= " --peaktype "
command+= results.collection7
command+= " --remove_artefacts "

#import os
#proc = subprocess.Popen( args=command, shell=True )
#proc.wait()

print command


data_dict={} 
for filename in results.collection2:
	infile = open(filename, 'r')
	print infile
	print("retrieving reads from file: %s", filename)
	for line in infile:
	    line = line.strip().split()
	    chr=line[0]
	    strand = line[5]
	    if strand == '+':
		pos = int(line[1])  # genomic position
		try: data_dict[chr][filename]['f'].append(pos)
		except KeyError:
		    if chr not in data_dict:
		        data_dict[chr] = {}
		    data_dict[chr][filename] = {}
		    data_dict[chr][filename]['f'] =[pos]
		    data_dict[chr][filename]['r'] =[]
	    elif strand == '-':
		pos = int(line[2])-1
		try: data_dict[chr][filename]['r'].append(pos)
		except KeyError:
		    if chr not in data_dict:
		        data_dict[chr] = {}
		    data_dict[chr][filename] = {}
		    data_dict[chr][filename]['f'] =[]
		    data_dict[chr][filename]['r'] =[pos]
	    else:
		print("strand error")
	infile.close()





import argparse
from subprocess import Popen, PIPE
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
parser.add_argument('--o1', type=str , dest='collection11',
                    help='pepr_peaks',
                    )
parser.add_argument('--o2', type=str , dest='collection12',
                    help='pepr_filtered peaks true',
                    )
parser.add_argument('--o3', type=str , dest='collection13',
                    help='pepr parameters',
                    )
parser.add_argument('--diff', type=str , dest='collection14',
                    help='Add diff values to a list',
                    )
parser.add_argument('--o4', type=str , dest='collection15',
                    help='pepr_peaks_diff diff true',
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
print 'output1       =', results.collection11
print 'output2       =', results.collection12
print 'output3       =', results.collection13
print 'diff          =', results.collection14


command = "-i "
command+=  ','.join(results.collection2)
command+= " -c "
command+=  ','.join(results.collection3)
command+=" -n "
command+= results.collection5
command+=" -o "
command+= results.collection11 
command+=" --o2 "
command+= results.collection12 
command+= " -f "
command+= results.collection6
command+= " --peaktype "
command+= results.collection7

if results.collection14 == 'true':
    command+= " --diff"
    command+=" --o4 "
    command+= results.collection15
if results.collection10 == 'true':
    command+= " --remove_artefacts "
print command

print 2
import shlex, subprocess
import os



p = subprocess.Popen([sys.executable, '/usr/lib/python2.6/site-packages/PePr/PePr.py']+command.split(), 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
for line in iter(p.stdout.readline, b''):
    	print(line)	

print 3 

print subprocess.PIPE





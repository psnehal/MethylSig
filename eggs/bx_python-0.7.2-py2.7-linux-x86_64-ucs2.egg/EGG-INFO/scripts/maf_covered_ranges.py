#!/afs/bx.psu.edu/project/pythons/py2.7-linux-x86_64-ucs2/bin/python2.7

"""
usage: %prog species1,species2,... nrequired < maf 
"""

import psyco_full

import bx.align.maf
import copy
import sys

from itertools import *
from bx.cookbook import doc_optparse

SPAN = 100
MIN = 100

def main():

    options, args = doc_optparse.parse( __doc__ )

    try:
        species = args[0].split(',')
        nrequired = int( args[1] )
    except:
        doc_optparse.exit()

    maf_reader = bx.align.maf.Reader( sys.stdin )
    
    interval_start = None
    interval_end = None   

    for m in maf_reader:            
        ref = m.components[0]
        # Does this alignment have enough of the required species        
        if nrequired <= len( [ comp for comp in m.components if comp.src.split('.')[0] in species ] ):
            if interval_start is None:
                interval_start = ref.start
                interval_end = ref.end
            else:
                if ref.start - interval_end < SPAN:
                    interval_end = ref.end
                else:
                    if interval_end - interval_start >= MIN: print ref.src.split('.')[1], interval_start, interval_end
                    interval_start = ref.start
                    interval_end = ref.end    
        else:
            if interval_start != None and interval_end - interval_start >= MIN: print ref.src.split('.')[1],interval_start,interval_end
            interval_start = None
            interval_end = None

if __name__ == "__main__": main()

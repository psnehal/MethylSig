import argparse
import pyRserve
parser = argparse.ArgumentParser()
parser.add_argument('--o', action='append', dest='collection1',
                    default=[],
                    help='Add repeated values to a list',
                    )
parser.add_argument('--i_file', action='append', dest='collection2',
                    default=[],
                    help='input file',
                    )
parser.add_argument('--s_id', action='append', dest='collection3',
                    default=[],
                    help='Add Samsple id to a list',
                    )
parser.add_argument('--data', action='append', dest='collection4',
                    default=[],
                    help='Add datatype values to a list',
                    )
parser.add_argument('--assem', type=str , dest='collection5',
                    help='Add datatype values to a list',
                    )
parser.add_argument('--destrand', action='append', dest='collection6',
                    default=[],
                    help='Add datatype values to a list',
                    )
parser.add_argument('--numcor', action='append', dest='collection7',
                    default=[],
                    help='Add datatype values to a list',
                    )
parser.add_argument('--cont', action='append', dest='collection8',
                    default=[],
                    help='Add datatype values to a list',
                    )
 
results = parser.parse_args()
conn= pyRserve.connect()
print "connected to Rserve"
conn.voidEval("library(methylSig)")
print 'simple_value     =', results.collection1
print 'constant_value   =', results.collection2
print 'boolean_switch   =', results.collection3
print 'collection       =', results.collection5


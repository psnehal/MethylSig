import argparse
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






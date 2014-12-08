#!/usr/bin/env python

import sys
import string
import sys, getopt

"""
histogram_gnuplot.py <datafile> <xtic column> <column_list> <title> <ylabel> <yrange_min> <yrange_max> <grath_file>
a generic histogram builder based on gnuplot backend

   data_file    - tab delimited file with data
   xtic_column  - column containing labels for x ticks [integer, 0 means no ticks]
   column_list  - comma separated list of columns to plot
   title        - title for the entire histrogram
   ylabel       - y axis label
   yrange_max   - minimal value at the y axis (integer)
   yrange_max   - maximal value at the y_axis (integer) 
                  to set yrange to autoscaling assign 0 to yrange_min and yrange_max
   graph_file   - file to write histogram image to
   img_size     - as X,Y pair in pixels (e.g., 800,600 or 600,800 etc.)
   
   
   This tool required gnuplot and gnuplot.py

anton nekrutenko | anton@bx.psu.edu

"""



assert sys.version_info[:2] >= ( 2, 4 )

def stop_err(msg):
    sys.stderr.write(msg)
    sys.exit()

def main(argv):
    skipped_lines_count = 0
    skipped_lines_index = []
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv) 
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
	   print 'test.py -i <inputfile> -o <outputfile>'
	   sys.exit()
        elif opt in ("-i", "--ifile"):
	   inputfile = arg
        elif opt in ("-o", "--ofile"):
	   outputfile = arg
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile
    try:
        in_file   = open( sys.argv[1], 'r' )
        xtic      = int( sys.argv[2] )
        col_list  = string.split( sys.argv[3],"," )
        title     = 'set title "' + sys.argv[4] + '"'
        
	print(in_file)
    except:
        stop_err("Check arguments\n")    
        sys.stderr.write('testing passing paramaeter to python code' %sys.argv[3] )
        
if __name__ == "__main__":
   main(sys.argv[1:])

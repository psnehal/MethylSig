"""
    Sorts tabular data on one or more columns. All comments of the file are collected
    and placed at the beginning of the sorted output file.
    
    usage: sorter.py [options]
    -i, --input: Tabular file to be sorted
    -o, --output: Sorted output file
    -k, --key: Key (see manual for bash/sort)
    
    usage: sorter.py input output [key ...]
	
	 -i inputFiles 
  -c chipFiles 
  -n ExperimentName 
  -f format 
  --peaktype=sharp 
  --remove_artefacts
  
   <command interpreter="python">axt_to_concat_fasta.py $dbkey_1 $dbkey_2 &lt; $axt_input &gt; $out_file1</command>
"""
# 03/05/2013 guerler

# imports
import os, re, string, sys
from optparse import OptionParser

# error
def stop_err( msg ):
    sys.stderr.write( "%s\n testing stdout" % msg )
    sys.exit()

# main
def main():
    # define options
	species1 = sys.argv[1]
	species2 = sys.argv[2]
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	sys.stderr.write( "%s\n" len(sys.argv) )
    # exit
    sys.exit(0)

if __name__ == "__main__":
    main()

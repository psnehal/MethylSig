#!/usr/bin/env python
''' The main .py file for the PePr pipeline '''

import re
import os
import sys


from classDef import Parameters

def main(argv):
    # initialize the logger 
    print "*************************inside pepr readfil*************************"
    # performing the option parser
    print argv
    opt = optParser.opt_parser(argv)
    parameter, readData = optParser.process_opt(opt)
    print parameter
    f = open('workfile', 'w')
    f.write('This is a test\n')
    f.write(parameter)
  
   
 
if __name__ == '__main__':
    try: main(sys.argv)
    except KeyboardInterrupt: 
        print "user interrupted me"

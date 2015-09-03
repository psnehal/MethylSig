#!/usr/bin/env Rscript

## begin warning handler)

suppressPackageStartupMessages(require(optparse))

option_list = list(
make_option(c("-a", "--avar"), action="store", default=NA, type='character',help="just a variable named assembly"),
make_option(c("-d", "--bvar"), action="store", default=NA, type='character',help="just a variable named destranded"),
make_option(c("-n", "--nvar"), action="store", default=NA, type='character',help="just a variable named numcores"),
make_option(c("-c", "--cvar"), action="store", default=NA, type='character',help="just a variable named context"),
make_option(c("-i", "--ivar"), action="store", default=NA, type='character',help="just a variable named input file"),
make_option(c("-s", "--svar"), action="store", default=NA, type='character', dest=sym,help="just a variable named sample file"),
make_option(c("-t", "--tvar"), action="store", default=NA, type='character',help="just a variable named datatype")

)
opt = parse_args(OptionParser(option_list=option_list))
 

# you can use either the long or short name
# so opt$a and opt$avar are the same.
cat("avar:\n")
cat(opt$avar)
cat("\n\na:\n")
cat(opt$a)
cat("\n\nd:\n")
cat(opt$d)
cat("\n\nn:\n")
cat(opt$n)
cat("\n\nc:\n")
cat(opt$c)
cat("\n\no:\n")
cat(opt$o)
cat("\n\ni:\n")
cat(opt$i)
cat("\n\ns:\n")
cat(opt$s)
cat("\n\nt:\n")
cat(sym)
cat("\n\nt:\n")
cat(opt$t)



if(!is.na(opt$avar) & !is.na(opt$bvar)) {
cat("here are strings a and b together at last:\n")
cat(paste(opt$a,opt$b,sep=''))
cat("\n\n")
} else {
cat("you didn't specify both variables a and b\n", file=stderr()) # print error messages to stderr
}   



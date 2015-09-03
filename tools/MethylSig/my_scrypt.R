#! /usr/bin/env Rscript

# http://cran.r-project.org/web/packages/optparse/vignettes/optparse.pdf
suppressPackageStartupMessages(library("optparse"))

option_list <- list(
    make_option(c('-d', '--date'), action='store', dest='date', type='character', default=Sys.Date(), metavar='"YYYY-MM-DD"', help='As of date to extract data from.  Defaults to today.')
)

opt <- parse_args(OptionParser(option_list=option_list))

# print(opt$date)
cat(sprintf('select * where contract_date > "%s"\n', opt$date)



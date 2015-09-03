#!/usr/bin/env Rscript

options(echo=TRUE) # if you want see commands in output file
args <- commandArgs(trailingOnly = TRUE)


xx= unlist(strsplit(args, ";", fixed = FALSE, perl = FALSE, useBytes = FALSE))
inputlist <- list() 
slist  <- list() 
tlist <- list() 

for ( i in 1:length(xx)) {
	
	if( grepl("-i",xx[i]) == TRUE)
	{
		print("found i")
		print(xx[i])
		inputlist[length(inputlist)+1] <-xx[i]

	}
	if( grepl("-s",xx[i]) == TRUE)
		{
			print("found s")
			print(xx[i])
			slist[length(slist)+1] <-xx[i]

		}
	if( grepl("-t",xx[i]) == TRUE)
		{
			print("found t")
			print(xx[i])
			tlist[length(tlist)+1] <-xx[i]

		}
}

trim <- function (x) gsub("^\\s+|\\s+$", "", x)
trim2 <- function( x ) {
  gsub("(^[[:space:]]+|[[:space:]]+$)", "", x)
}

print("***************************************************")
test = gsub("-i ", "", inputlist[1])
inputFiles =""
fileList = c()

for (i in 1:length(inputlist))
{
	str = gsub("-i ", "", inputlist[i])
	str = trim(str)
	print( str)
	fileList[i] <- str

}


sampleId =""
sampleID = c()
for (i in 1:length(slist))
{	
	slisttr = gsub("-s ", "", slist[i])
	slisttr = trim(slisttr)
	sampleID[i]=slisttr
		
}


treat= ""
treatment = c()
for (i in 1:length(tlist))
{
	print(tlist[i])
	tlisttr = gsub("-t", "", tlist[i])
	tlisttr = trim(tlisttr)
	treatment[i]=as.numeric(tlisttr)
}

library(methylSig)
meth <- methylSigReadData(fileList, sample.ids = sampleID, assembly = "hg18",treatment = treatment, context = "CpG", destranded=TRUE)
print(meth)
write.table(meth, file="mymatrix.txt", row.names=FALSE, col.names=FALSE)




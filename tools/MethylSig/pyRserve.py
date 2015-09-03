import pyRserve
import numpy
conn= pyRserve.connect()
conn.voidEval("library(methylSig)")
conn.r.fileList = numpy.array(['/home/snehal/galaxy-dist/database/files/000/dataset_34.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_35.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_36.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_37.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_38.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_39.dat'])
conn.r.samid = numpy.array(["AML1", "AML2", "AML3", "NBM1", "NBM2", "NBM3"])
conn.r.treatment=  numpy.array([1,1,1,1,0,0,0,0])
conn.r.assembly ="hg18"
conn.r.context ="CpG"
conn.voidEval("meth <- methylSigReadData(fileList, sample.ids = samid, assembly = assembly,treatment = treatment, context = context, destranded=TRUE)")
conn.voidEval("methTile = methylSigTile(meth,win.size = 25)")


Error in (methSigObject$creads + methSigObject$treads > 0)[group2, ] : 
  subscript out of bounds





For R:
 fileList=c('/home/snehal/galaxy-dist/database/files/000/dataset_34.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_35.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_36.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_37.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_38.dat', '/home/snehal/galaxy-dist/database/files/000/dataset_39.dat')
methylSigCalc(meth, groups = c(Treatment = 1, Control = 0), dispersion = "both",local.disp = FALSE, wins ize.disp = 200, min.per.group = c(3, 3),weightFunc=methylSig_weightFunc, num.cores = 1)




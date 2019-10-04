
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:38:10 2017
Purpose: create a orthomosaice from the images 
@author: abhilam
"""
import os
import PhotoScan
import glob
from Create_orthomosaic_Agisoft import OrthoMosaic


WorkingPth='D:\\Ray_Corn_17\\Creating_Mosaic\\' # working directory
os.chdir(WorkingPth)
destPath=WorkingPth

#DateofFolder=['20170607','20170614','20170630','20170703','20170718','20170807','20170920']#['20170614']#'20170607',
DateofFolder=['20170703','20170725','20170807','20171002']#[]# X3#'20170607','20170614','20170630',

pth='D:\\Ray_Corn_17\\FFF\\Locations\\Scandia\\X3'
global doc
doc = PhotoScan.app.document 
PsxNme=pth.split('\\')[-2]+'_'+pth.split('\\')[-1]
doc.save(PsxNme+'.psx')
for fold in DateofFolder:

	SrcPath=pth+fold
	P2File=pth+'\\'+fold
	fnme=pth.split('\\')[-2]+'_'+pth.split('\\')[-1]+'_'+fold
	print (P2File)
	print (destPath)
	print (fnme)
	print (destPath+fnme)
	OrthoMosaic(P2File,destPath,fnme)

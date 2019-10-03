# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:38:10 2017
Purpose: create a orthomosaice from the images 
@author: abhilam
"""
import os
import PhotoScan
import glob

def OrthoMosaic(srcPth,DestPath,fname):
	#global doc
    #app = QtGui.QApplication.instance()
    # srcPth= Source of Image File
	# DestPath= directory where you save orthomosaic
	# Create photoscan application
	#app = QtGui.QApplication.instance()
	chunk=doc.addChunk()
	chunk = doc.chunks[-1]
	chunk.label = fname
	
	#image_list=os.listdir(P2File)
	extensions=["*.TIF", "*.PNG","*.jpg","*.tiff"]#"*.JPG","*.JPEG",
	Photo_list = []
	for extension in extensions :
		Photo_list.extend(glob.glob(srcPth+"/"+extension))
		
	#Photo_list=list()
	#for photo in image_list:
	#	print(photo)
	#	if photo.rsplit(".",1)[1].upper() in ["JPG", "JPEG", "TIF", "PNG","jpg"]:
	#		   Photo_list.append(P2File + photo)
	#		   #print (Photo_list[-1])
	#		   #print(photo)
	#	else:
	#		   #print("No photo available.")
	#		   pass
	#print(Photo_list)
	chunk.addPhotos(Photo_list)
	doc.save()
	PhotoScan.app.update()
	#PhotoScan.app.cpu_cores_inactive = 2  #CPU cores inactive
	# Align Photos
	chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, # can choose Highest or medium
					  preselection=PhotoScan.Preselection.NoPreselection,\
					  generic_preselection=True,\
					  reference_preselection=True,\
					  filter_mask=False,\
					  keypoint_limit=40000, # Maximum number of key points to look for in each photo
					  tiepoint_limit=4000,   # Maximum number of tie points to generate for each photo
					  )                    
	chunk.alignCameras()
	doc.save()
	PhotoScan.app.update() 

	#PhotoScan.app.document.chunk.alignCameras()
	"""
	chunk.buildDenseCloud(quality=PhotoScan.HighQuality,\
						  filter=PhotoScan.FilterMode.AggressiveFiltering)
	"""
	# Creating Mesh
	chunk.buildModel(surface=PhotoScan.SurfaceType.HeightField,\
					 
					 face_count=PhotoScan.FaceCount.HighFaceCount,\
					 
					 interpolation=PhotoScan.EnabledInterpolation)
	# Adding Texture
	chunk.buildUV(mapping=PhotoScan.MappingMode.GenericMapping)
	chunk.buildTexture(blending=PhotoScan.MosaicBlending,\
					   color_correction=True,\
					   fill_holes=True,\
					   size=4096*4)
	print('done building Texture')
	doc.save()
	print('done saving Texture')

	PhotoScan.app.update() 
	print('done updating Texture')

	"""
	doc.chunk.buildDem(source=PhotoScan.DataSource.DenseCloudData,\
					   interpolation=PhotoScan.EnabledInterpolation,\
					   projection=PhotoScan.CoordinateSystem("EPSG::4326"))
	"""
		
	chunk.buildOrthomosaic()
	print('done building OM')

	doc.save()
	print('done saving PSX after OM')
	PhotoScan.app.update()
	print('done updating after OM')


	chunk.exportOrthomosaic(DestPath+fname + ".tif")
	#doc.clear()
	return()
	
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

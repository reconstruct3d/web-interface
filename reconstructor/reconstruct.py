from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

import os
import sys

sys.path.insert(0, '/root/FYP/SfM/src')
from featmatch import *
from sfm import *

CAL_MATRIX = 0

from .models import Image

def reconstruct(request):
	"""
	Perform the reconstruction process.
	"""
	# Perform validation.
	if request.method == 'POST':
		calibration = ['benchmark', 'lg_g3']
		#imgNames = ['/root/FYP/SfM/data/fountain-P11/images/0004.jpg','/root/FYP/SfM/data/fountain-P11/images/0005.jpg',
                #'/root/FYP/SfM/data/fountain-P11/images/0005.jpg']
		fileName = 'reconstructor/static/ply/new.ply'

		parser = argparse.ArgumentParser()
		SetArgumentsFeatMatch(parser)
		opts = parser.parse_args()
		FeatMatch(opts)

		# Run the SfM pipeline.
		parser = argparse.ArgumentParser()
		SetArguments(parser)
		opts = parser.parse_args()
		PostprocessArgs(opts)

		sfm = SFM(opts)
		sfm.Run()
		#main(opts, imgNames, fileName)
		#path = os.environ['RECONSTRUCTOR_PATH']

		# Get all images using session ID.
		images = Image.objects.filter(session_id = request.session.session_key)

		# Import the library.
		
		# Send file paths to all images.
		imgNames = []
		for image in images:
			print(image.file_name)
			imgNames.append('/root/FYP/web-interface/images/' + image.file_name)
		# main(opts, imgNames, fileName)
	
		return HttpResponse('test')
	# return render(
	#	request,
	#	'index.html',
	# )

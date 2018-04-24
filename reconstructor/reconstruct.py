from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

import sys
import os
sys.path.insert(0, '/root/FYP/SfM/src')
from main import *

# from pathlib import Path
from .models import Image

def reconstruct(request):
	"""
	Perform the reconstruction process.
	"""
	# Perform validation.
	if request.method == 'POST':
		imgNames = ['/root/FYP/SfM/data/fountain-P11/images/0004.jpg','/root/FYP/SfM/data/fountain-P11/images/0005.jpg',
                '/root/FYP/SfM/data/fountain-P11/images/0005.jpg']

		parser = argparse.ArgumentParser()
		SetArguments(parser)
		opts = parser.parse_args()
		main(opts, imgNames)
		#path = os.environ['RECONSTRUCTOR_PATH']

		# Get all images using session ID.
		#images = Image.objects.filter(session_id = request.session.session_key)

		# Import the library.
		
		# Send file paths to all images.
		#for image in images:
		#	print(image.file_name)
	
		return HttpResponse('test')
	# return render(
	# 	request,
	# 	'index.html',
	# )

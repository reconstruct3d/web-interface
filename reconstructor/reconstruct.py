from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

import os
# from pathlib import Path
from .models import Image

def reconstruct(request):
	"""
	Perform the reconstruction process.
	"""
	# Perform validation.
	if request.method == 'POST':

		path = os.environ['RECONSTRUCTOR_PATH']

		# Get all images using session ID.
		images = Image.objects.filter(session_id = request.session.session_key)

		# Import the library.
		
		# Send file paths to all images.
		for image in images:
			print(image.file_name)
	
		return HttpResponse('test' + path)
	# return render(
	# 	request,
	# 	'index.html',
	# )


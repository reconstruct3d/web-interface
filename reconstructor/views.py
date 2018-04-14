from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

from .models import Image

def index(request):
	"""
	View function for home page of site.
	"""
	return render(
		request,
		'index.html',
	)

def perform(request):
	"""
	Store the images and perform the reconstruction process.
	"""
	# Perform validation.
	if request.method == 'POST':
		# Get the file.
		file = request.FILES['files[]']

		# Save the file to a temporary location.
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)

		# Create a database entry.
		image = Image(
					file_name = filename,
					file_size = file.size,
					file_format = file.content_type,
					session_id = request.session.session_key,
					date_created = timezone.now
				)
		image.save()



		response_data = {}
		response_data['result'] = 'test'
		return JsonResponse({ 'name': filename })
		# return render(
		# 	request,
		# 	'test.html',
		# )

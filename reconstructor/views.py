from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

import os
import shutil
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

"""List all the steps involved in reconstruction"""
def procedure(request):
	if request.method == 'GET':
		return render(
			request,
			'how-it-works.html',
		)

"""Return the contacts page"""
def contact(request):
	if request.method == 'GET':
		return render(
			request,
			'contact.html',
		)


"""Delete all existing images (from database and directory)"""
def reset(request):
	if request.method == 'GET':
		# Clear the directory.
		# shutil.rmtree('/media/adeel/643459A034597650/Academics/Semester VIII/FYP-II/code/web_interface/images')
		# os.makedirs('/media/adeel/643459A034597650/Academics/Semester VIII/FYP-II/code/web_interface/images')

		shutil.rmtree('/root/FYP/web-interface/images')
		os.makedirs('/root/FYP/web-interface/images')

		# Remove records from database.
		Image.objects.all().delete()
		return JsonResponse({ 'status': 'success' })

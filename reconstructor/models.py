from django.db import models

class Image(models.Model):
	session_id = models.CharField(max_length=60)
	file_name = models.CharField(max_length=60)
	file_size = models.IntegerField()
	file_format = models.CharField(max_length=10)
	date_created = models.DateTimeField(auto_now_add=True)

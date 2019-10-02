from django.db import models

# Create your models here.

class Page(models.Model): 
	title = models.CharField(max_length = 100)
	content = models.TextField()
	last_updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self): # new
		return "/detail/%i" % self.id
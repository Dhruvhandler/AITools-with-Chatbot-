from django.db import models

# Create your models here.
class Person(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)

class category(models.Model):
	category_name=models.CharField(max_length=100, primary_key=True)
	def __str__(self):
			return self.category_name

class structure(models.Model):
	category_name=models.ForeignKey(category, on_delete=models.CASCADE)
	tool_name=models.CharField(max_length=100)
	tool_image=models.ImageField(upload_to="data",blank=True)
	tool_description=models.TextField()
	tool_link=models.URLField(max_length=500)

class article(models.Model):
	title=models.CharField(max_length=500)
	Description=models.TextField()
	image=models.ImageField(upload_to="data",blank=True)
	date=models.DateField()
	by=models.CharField(max_length=200)

class initiative(models.Model):
	title=models.CharField(max_length=500)
	image=models.ImageField(upload_to="data",blank=True)
	profile=models.TextField()
	Description=models.TextField()

class video(models.Model):
	title=models.CharField(max_length=100)
	video=models.FileField()

class faq(models.Model):
	ques=models.TextField()
	ans=models.TextField()

class contactus(models.Model):	
	Name=models.CharField(max_length=100)
	email_id=models.EmailField()
	message=models.CharField(max_length=500)
			
class userregister(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

class review(models.Model):
	name=models.CharField(max_length=100)
	message=models.CharField(max_length=500)	

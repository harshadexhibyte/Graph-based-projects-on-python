from django.db import models

# Create your models here.
class userMaster(models.Model):
	fname=models.CharField(max_length=100)
	mname=models.CharField(max_length=100)
	email=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100,default="")
	cpassword=models.CharField(max_length=100,default="")
	

	def __str__(self):
		return self.mname+" "+self.email
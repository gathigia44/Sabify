from django.db import models


class User(models.Model):
	id = models.AutoField(primary_key=True)
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	username=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	number=models.CharField(max_length=30)
	repwd=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	street=models.CharField(max_length=30)
	area=models.CharField(max_length=30)
	country=models.CharField(max_length=30)



	

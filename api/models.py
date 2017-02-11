from django.db import models

# Create your models here.
class Disease(models.Model):
	name=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.name

class Symptom(models.Model):
	name=models.TextField(unique=False)
	totalfrequency=models.IntegerField(default=0)
	def __unicode__(self):
		return self.name

class SymptomDisease(models.Model):
	disease=models.OneToOneField(Disease,on_delete=models.CASCADE)
	symptom=models.OneToOneField(Symptom,on_delete=models.CASCADE)
	symptomfrequency=models.IntegerField(default=0)
	def __unicode__(self):
		return "Sympton Disease Transaction"

class NaturalRemedy(models.Model):
	title=models.TextField(unique=False,default="default")
	disease= models.ForeignKey(to=Disease,related_name="members", null=True, blank=True,unique=False)
	remedy=models.TextField(unique=False)
	def __unicode__(self):
		return self.title

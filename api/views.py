from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def getSymptoms(request):
	try:
		response=request.GET.get("symptom1")
		print response
	except Exception as e:
		return HttpResponse("There was an error")

	return HttpResponse("Post Success")

from django.contrib import admin
from api.models import Disease,Symptom,SymptomDisease,NaturalRemedy
# # Register your models here.

admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(SymptomDisease)
admin.site.register(NaturalRemedy)
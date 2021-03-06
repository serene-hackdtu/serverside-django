import csv
import random
import math
def loadcsv(filename):
	lines=csv.reader(open(filename,"rb"))
	dataset=list(lines)
	for i in range(len(dataset)):
			dataset[i]=[float(x)for x in dataset[i]]
	return dataset

def seperateByDisease(dataset):
	seperated={}
	for i in range(len(dataset)):
		vector=dataset[i]
		if vector[-1] not in seperated:
			seperated[vector[-1]]=vector
	return seperated
def gets(filename):
	symptoms={}
	ab=csv.reader(open(filename,"rb"))
	dataset=list(ab)
	for i in range(len(dataset)):
		vector=dataset[i]
		if vector[0] not in symptoms:
			symptoms[int(vector[0])]=vector[1]		
	return symptoms


def ps(summaries):
	prob={}
	sum=0
	for classvalue,instances in summaries.iteritems():
		sum=sum+summaries[classvalue]
	for classvalue,instances in summaries.iteritems(): 
		p=summaries[classvalue]/sum
		prob[classvalue]=p
	return prob

def summarize(dataset):
	summaries=[(getsum(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries
def summarizeByDisease(dataset):
	seperated={}
	seperated=dataset
	summaries={}
	vector=[]
	for classvalue,instances in seperated.iteritems():
		sum=0
		vector=instances
		for value in vector:
			sum=sum+value
		summaries[classvalue]=sum
	return summaries

def summarizeBysymptom(dataset):
	summaries={}
	a=[0,0,0,0,0,0]
	for j in dataset:
		for k in range (len(j)-1):
			a[k]=a[k]+j[k]
	for k in range (len(dataset[0])-1):
		summaries[k]=a[k]
	return summaries

def nbc(classes,getdi,symptom,getsym,asb,traindata):
	sym=summarizeBysymptom(traindata)
	dis=summarizeByDisease(classes)
	pod=ps(dis)
	pos=ps(sym)
	maxp=0.0
	pf=0.0
	in1=0

	for classvalue,instances in classes.iteritems():
		pf=0.0
		for i in range(5):
			if asb[getsym[i]]==1 :
				p1=instances[i]
				p2=dis[classvalue]
				p=p1/p2
				pf=pf+p*pos[i]
		pf=pf/pod[classvalue]
		if(pf>maxp):
			maxp=pf
			in1=classvalue
	return in1

def mainf(*args):
	getsym={}
	filename="/home/sukhad/symptom.csv"
	getsym=gets(filename)
	asb={}
	symptoms=[]
	for key in getsym:
		asb[getsym[key]]=0
	for arg in args:
		asb[arg]=1
	for key in getsym:
		if asb[getsym[key]]==1:
			symptoms.append(key)
	filename1="/home/sukhad/disease.csv"
	getdi={}
	getdi=gets(filename1)
	filename2="/home/sukhad/diabetes.csv"
	traindata=loadcsv(filename2)
	classes=seperateByDisease(traindata)
	in1=nbc(classes,getdi,symptoms,getsym,asb,traindata)
	return getdi[in1]







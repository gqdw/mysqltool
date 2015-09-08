from django.shortcuts import render
from django import forms
# Create your views here.

class MysqlForm( forms.Form):
	ip = forms.GenericIPAddressField()
	user = forms.CharField(max_length=30)
	password = forms.CharField(max_length=60)

def index( request):
	if request.method == 'POST':
		form = MysqlForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print cd['ip'], cd['user'] ,cd['password']

	else:
		form = MysqlForm()
	return render(request,'index.html',{ 'form':form })

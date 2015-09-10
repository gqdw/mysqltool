from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from main import MysqlInfo
# Create your views here.

class MysqlForm( forms.Form):
	host = forms.GenericIPAddressField()
	user = forms.CharField(max_length=30)
	password = forms.CharField(max_length=60,initial='')
	dbname = forms.CharField(max_length=30)

def index( request):
	if request.method == 'POST':
		form = MysqlForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print cd['host'], cd['user'] ,cd['password'],cd['dbname']
			n1 = MysqlInfo( cd['user'],cd['password'] ,cd['host'],cd['dbname'])
			n1.get_mysql_info()
			n1.write_to_excel()
#			return HttpResponse('ok')
			return render(request,'list.html',{'infos':n1.infos})

	else:
		form = MysqlForm()
	return render(request,'index.html',{ 'form':form })

#def test( request ):
	

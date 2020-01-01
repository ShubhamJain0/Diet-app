from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Dietdata



# Create your views here.
def homepage(request):
	return render(request, "homepage.html")


def detailspage(request):
	return render(request, "form.html")


		

def data(request):
	query=request.POST.get('q', None)
	context={"query":query}
	if query is not None:
		Dietdata.objects.create(query=query)
		blog_list=Dietdata.objects.search(query=query)
		context['blog_list']=blog_list
	return render(request, 'data.html', context)







	

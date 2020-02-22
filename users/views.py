from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
def logout(request):
	"""注销用户"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
	
	
	

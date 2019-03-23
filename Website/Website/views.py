from django.shortcuts import render
from django.http import HttpResponse

from .forms import Login


def index(request):

	# formlogin = Login()

	# context = {

	# 	'formLogin':formlogin,

	# }

	return render(request, 'index.html')


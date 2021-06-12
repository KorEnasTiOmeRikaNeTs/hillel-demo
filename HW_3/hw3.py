import sys

from random import choice
from string import ascii_letters
from string import digits

from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect

ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='qazwsx'
TEMPLATES = [
 	{
 		'BACKEND': 'django.template.backends.django.DjangoTemplates',
 		'DIRS': [''],
 	}
]

dict_with_key_and_link = dict()

def almost_all_the_work(request):
	list_with_filter_link = []
	list_with_key = []
	if request.POST:
		link = request.POST.get('url', '')
		if link.startswith(('http://', 'https://', 'ftp://')):
			key = ''.join(choice(''.join([ascii_letters, digits])) for _ in range(5))
			dict_with_key_and_link[key] = link
			return render(request, 'template_hw3.html', {'something': key,
														 'sss': dict_with_key_and_link})
		else:
			return render(request, 'template_hw3.html', {'others': f'Invalid URL {link}. Allowed schemes: http://,ftp://,https://'})
	else:
		return render(request, 'template_hw3.html', {})

def redirect_from_short_to_long(request, key):
	if key in dict_with_key_and_link:
		return redirect(dict_with_key_and_link[key])
	else:
		return redirect('/')

urlpatterns = [
	path("", almost_all_the_work),
	path("<key>", redirect_from_short_to_long)
]

if __name__ == "__main__":
	execute_from_command_line(sys.argv)


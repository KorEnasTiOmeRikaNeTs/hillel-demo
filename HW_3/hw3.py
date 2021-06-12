import sys

from random import choice
from string import ascii_letters
from string import digits

from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render



ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='qazwsx'
TEMPLATES = [
 	{
 		'BACKEND': 'django.template.backends.django.DjangoTemplates',
 		'DIRS': [''],
 	}
]


# text = ''.join(this.d.get(c, c) for c in this.s)
# title, _, *quotes = text.splitlines()

dict_with_key_and_link = dict()

def almost_all_the_work(request):
	list_with_filter_link = []
	list_with_key = []
	if request.POST:
		link = request.POST.get('url', '')
		if link.startswith('http') or link.startswith('https') or link.startswith('ftp'):
			key = ''.join(choice(''.join([ascii_letters, digits])) for _ in range(5))
			list_with_filter_link.append(link)
			list_with_key.append(key)
			dict_with_key_and_link = dict(zip(list_with_key, list_with_filter_link))
			short_link = f'<h1><a href = "{key}">{key}</a><h1>'
			return render(request, 'template_hw3.html', {'something': short_link})
		else:
			return render(request, 'template_hw3.html', {'others': f'Invalid URL {link}. Allowed schemes: http,ftp,https'})
	else:
		return render(request, 'template_hw3.html', {})

	# return render(request, 'template_hw3.html', {'title': 'Title',
	#											 'template': TEMPLATES,
	#											 'quote': "quotes"})

def redirect_from_short_to_long(_):
	pass


	# return render(request, "template_hw3.html", {'quote': print("Hello_World")})

urlpatterns = [
	path("", almost_all_the_work),
	path("<key>", redirect_from_short_to_long)
]

if __name__ == "__main__":
	execute_from_command_line(sys.argv)


import sys

from random import choice

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
 		'DIRS': []
 	}
]


# text = ''.join(this.d.get(c, c) for c in this.s)
# title, _, *quotes = text.splitlines()


def hello(request):
	return render(request, 'template_hw3.html', {'title': 'Title',
												 'template': TEMPLATES})

def redirect_from_short_to_long(_):
	pass

urlpatterns = [
	path("", hello),
	path("fff", redirect_from_short_to_long)
]

if __name__ == "__main__":
	execute_from_command_line(sys.argv)


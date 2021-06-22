import sys
import os

from random import choice
from string import ascii_letters, digits

from django.core.management import execute_from_command_line
from django.urls import path
from django.shortcuts import render, redirect

from pathlib import Path
from django.db import connection

ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='qazwsx'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = [
 	{
 		'BACKEND': 'django.template.backends.django.DjangoTemplates',
 		'DIRS': [BASE_DIR],
 	}
]
BASE_DIR_ = Path(__file__).resolve().parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR_ / 'hw4.sqlite3'
    }
}

create = 'CREATE TABLE IF NOT EXISTS hw4_table_with_key_and_link (key char(5), link text)'
with connection.cursor() as cur:
	cur.execute(create)

def almost_all_the_work(request):
	key = ''
	if request.POST:
		link = request.POST.get('url', '')
		query = 'SELECT key FROM hw4_table_with_key_and_link WHERE link = %s'
		with connection.cursor() as cur:
			cur.execute(query, [link])
			key = cur.fetchone()
		if key:
			return render(request, 'template_hw4.html', {'key': key[0]})
		else:
			if link.startswith(('http://', 'https://', 'ftp://')):
				key = ''.join(choice(''.join([ascii_letters, digits])) for _ in range(5))
				with connection.cursor() as cur:
					insert = 'INSERT INTO hw4_table_with_key_and_link (key, link) VALUES (%s, %s)'
					cur.execute(insert, [key, link])
				return render(request, 'template_hw4.html', {'key': key})
			else:
				return render(request, 'template_hw4.html', {'others': f'Invalid URL {link}. Allowed schemes: http://,ftp://,https://'})
	else:
		return render(request, 'template_hw4.html', {})

def redirect_from_short_to_long(request, key):
	query = 'SELECT link FROM hw4_table_with_key_and_link WHERE key = %s'
	with connection.cursor() as cur:
		cur.execute(query, [key])
		link = cur.fetchone()
	if link:
		return redirect(link[0])
	else:
		return redirect('/')

urlpatterns = [
	path("", almost_all_the_work),
	path("<key>", redirect_from_short_to_long)
]

if __name__ == "__main__":
	execute_from_command_line(sys.argv)


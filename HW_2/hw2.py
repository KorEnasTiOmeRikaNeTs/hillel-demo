import sys

from importlib import import_module
from importlib.util import find_spec

from django.core.management import execute_from_command_line
from django.http import HttpResponseNotFound
from django.shortcuts import render

from django.urls import path

# configutation
ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='qazwsx'
TEMPLATES =[  
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
 		'DIRS': [],
	}
]


def creating_links(module_name):
	# checking the module exists
	module_spec = find_spec(module_name)                                     
	if module_spec is None:													 		
		HttpResponseNotFound(f'module {module_name} is not found')   
	else:
		import_module(module_name)

	# filter the module	
	module_doc = list()

	for atr in dir(module_name):
		if atr[0] == "_":
			pass
		else:
			module_doc.append(atr)

    # creating links    	
	for i in range(0, len(module_doc) - 1):
		str_with_link = f'<a href = "doc/{module_name}/{module_doc[i]}">{module_doc[i]}</a>'
		return str_with_link



def fun_module_doc(request, module_name):
	return render(request, "template_HW_2.html", {'module_ottrs': creating_links(module_name)})
										  			
		

def fun_obj_doc(request, module_name, name):
	return render(request, "template1_HW_2.html", {'ottrs_doc': module_name.name.__doc__})

urlpatterns = [
	path("doc/<module_name>", fun_module_doc),
	path("doc/<module_name>/<name>", fun_obj_doc)
]

import this
if __name__ == "__main__":
	execute_from_command_line(sys.argv)





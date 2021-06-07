import sys

from importlib import import_module

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponseNotFound
from django.http import HttpResponse

from django.urls import path

# configutation
ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='qazwsx'

template = '''
<!DOCTYPE html>
<html>
<head>
 <title>{title}</title>
</head>
<body>
 <div>{module_ottrs}</div>
</body>
</html>
'''

template1 = '''
<!DOCTYPE html>
<html>
<head>
 <title></title>
</head>
<body>{ottr_doc}</body>
</html>
'''

def fun_module_doc(request, module_name):
	try:
		module = import_module(module_name)
	except ModuleNotFoundError:
		return HttpResponseNotFound(f'No module named "{module_name}"')
	long_str_with_links = ""
	list_with_links = []
	module_doc = []
	# filter the module	
	for attr in dir(module):
		if attr[0] == "_":
			pass
		else:
			module_doc.append(attr)
    # creating links
	for i in range(0, len(module_doc)):
		str_with_link = f'<a href = "{module_name}/{module_doc[i]}">{module_doc[i]}</a><br>'
		list_with_links.append(str_with_link)
	long_str_with_links = "".join(list_with_links)
	return HttpResponse(template.format(title=f'index of {module_name}', module_ottrs=long_str_with_links))								  			
		

def fun_obj_doc(request, module_name, name):
	try:
		module = import_module(module_name)
	except ModuleNotFoundError:
		return HttpResponseNotFound(f'No module named "{module_name}"')
	try:
		ottr = getattr(module, name)
	except AttributeError:
		return HttpResponseNotFound(f'module "{module_name}" has no attribute "{name}"')
	return HttpResponse(template1.format(ottr_doc=f'<pre style="word-wrap: break-word; white-space: pre-wrap;">{ottr.__doc__}</pre>'))
	

urlpatterns = [
	path("doc/<module_name>", fun_module_doc),
	path("doc/<module_name>/<name>", fun_obj_doc)
]


if __name__ == "__main__":
	execute_from_command_line(sys.argv)





import sys, csv
from uuid import UUID
from collections import defaultdict
from math import ceil


def simple_field(type_, field):
	def _inner(data):
		for val in data:
			type_(val)
		return field
	return _inner


def char_field(data):
	max_lenght = ceil(max(map(len, dataf)) * 1,25/10) * 10
	return f'char_field(max_lenght={max_lenght})'


def gen_field(name, data):
	validator = [simple_field(int, 'IntegerField()'), simple_field(float, 'FloatField()'), simple_field(UUID, 'UUIDField()'), char_field]
	for v in validator:
		try:
			field = v(data)
			break
		except:
			pass
	indent = ' ' * 4
	try:
		print(f'{indent}{name} = model.{field}')
	except:
	 	print('Yours .csv file cant be read correctly. Please try another file')



def gen_model(fname, col_data):
	print(f'class {fname}(model.Model):')
	for k, v in col_data.items():
		gen_field(k, v)


def process_file(fname):
	with open(fname) as csvfile:
		reader = csv.DictReader(csvfile)
		col_data = defaultdict(set)
		for row in reader:
			for k, v in row.items():
				col_data[k].add(v)
	return col_data


if __name__ == '__main__':
	args = sys.argv[1:]
	if args:
		gen_model(args[0], process_file(args[0]))
	else:
		print('please, enter the file')

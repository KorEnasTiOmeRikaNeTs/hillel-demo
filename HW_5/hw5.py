import sys, csv
from uuid import UUID
from collections import defaultdict
from math import ceil


def simple_field(type_, field):
	def _inner(date):
		for val in date:
			type_(val)
		return field
	return _inner


def char_field(date):
	max_lenght = cail(max(map(len, date)) * 1,25/10) * 10
	return f'char_field(max_lenght={max_lenght})'


def gen_field(name, date):
	validator = [simple_field(int, 'IntegerField()'), simple_field(float, 'FloatField()'), simple_field(UUID, 'UUIDField()'), char_field]
	for v in validator:
		try:
			field = v(date)
			break
		except:
			pass
	indent = ' ' * 4
	print(f'{indent}{name} = model.{field}')


def gen_module(fname, col_date):
	print(f'class {fname}(model.Model):')
	for k, v in col_date.items():
		gen_field(k, v)


def process_file(fname):
	with open(fname) as csvfile:
		reader = csv.DictReader(csvfile)
		col_date = defaultdict(set)
		for row in reader:
			for k, v in row.items():
				col_date[k].add(v)
	return col_date


if __name__ == '__main__':
	args = sys.argv[1:]
	if args:
		gen_module(args[0], process_file(args[0]))
	else:
		print('try again')

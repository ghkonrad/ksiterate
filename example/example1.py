#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ksiterate

itspec = [
	{
		'A':[1, 2, 3],
		'B':[10, 11, 12],
		'C':[20, 21]
	},
	{
		'A':[5, 6,],
		'B':[13, 14],
		'C':[21, 22, 23]
	}
	];

itspec2 = [
	{
		('A', 'B'):[(1, 10), (2, 11), (3, 12)],
		'C':[20, 21]
	}
	];


it = ksiterate.Iteration(itspec);

for i in it.iterate():
	print(i);

print("-"*30);

for i in it.iterate(include_params={"C",}):
	print(i);
	for j in it.iterate(i,):
		print(j);

print("-"*30);

it2 = ksiterate.Iteration(itspec2);
for i in it2.iterate():
	print(i);

print("-"*30);

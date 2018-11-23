#!/usr/bin/env python

class HDU_list(object):
	def __init__(self):
		self.n_files = 0
		self.list    = []
		
class HDU_struct(object):
	def __init__(self):
		self.name    = ''
		self.dim     = [0,0] # should this be a Numpy array?
		self.type    = ''
		

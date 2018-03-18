#!/usr/bin/env python3

# Licence: 

# Usage:

import sys
import argparse
import numpy as np

parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
parser.add_argument(dest="input_file", help="Input file")
parser.add_argument("--het_loci", help="Outputs the names of the heerozygous sites for each individual")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

class Individual(object):
	### NOT IN USE ###
	def __init__(self, name, locus_names, het_states):
		self.name = name
		self.locus_names = locus_names
		self.het_states = het_states
	
	# Allele states
	# 0: Missing data
	# 1: Homozygous
	# 2: Heterozygous

	def get_het_locus(self):
		het_loci = []
		pos = 0
		for state in self.het_states:
			if int(state) == 2:
				het_loci.append(self.locus_names[pos])
			pos += 1
		return het_loci

	def get_state(self, locus_number):
		return int(self.het_states[locus_number])

	def __str__(self):
		return self.name


def main():

	### Read in the data and stor it in an array ###

	data = open(args.input_file)
	individuals = []

	# Generate a list of Locus names
	first_line = True
	locus_names = []
	matrix_list = []
	for line in data.readlines():
		# The first line contains the locus names
		if first_line:
			for locus_name in line.split(","):
				# The last column has no name but includes a new line character
				locus_name = locus_name.rstrip("\n")
				# Every second locus is inheriting its name from the previous column
				if locus_name != " ":
					name = locus_name
					sufix = "_a"
				else:
					sufix = "_b"
				locus_name = name + sufix
				# Skip first column
#				if locus_name == "_a":
#					pass
#				else:
#					locus_names.append(locus_name)
				matrix_list.append(locus_name)
				dim1 = len(matrix_list)
#			matrix_list.append(locus_names)
			first_line = False
		# Subsequent lines contains the locus data from each individual.
		else:
			for x in line.split(","):
				matrix_list.append(x)


	dim2 = int(len(matrix_list) / dim1)
#			new_line = []
#			for state in line.split(","):
#				new_line.append(state)
#			matrix_list.append(new_line)

#	matrix = np.arange(len(matrix_list)).reshape(dim1, dim2)
	matrix = np.array(matrix_list).reshape(dim2, dim1)
	print(matrix) 

	for row in matrix:
		print(row)

	for column in matrix.T:
		print(column)

#	for row in matrix:
#		print(row)

#	print(matrix.shape)

#	locus_number = 0
#	for x in np.nditer(matrix):
#		print(x)
#		for (x,y), value in numpy.ndenumerate(a):
#		print(matrix[0][x])
#		no_data = 0
#		hom = 0
#		het = 0
#		for individual in individuals:
#			state = individuals[locus_number].get_state(locus_number)
#			if state == 0:
#				no_data += 1
#			if state == 1:
#				hom += 1
#			if state == 2:
#				het += 1
#		locus_number += 1
#		print(locus, no_data, hom, het)

if __name__ == "__main__":
    main()

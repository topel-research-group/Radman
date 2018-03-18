#!/usr/bin/env python3

# Licence: 

# Usage:

import sys
import argparse
import numpy as np

parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
zygosity_group = parser.add_mutually_exclusive_group(required=True)
parser.add_argument(dest="input_file", help="Input file")
zygosity_group.add_argument("--hom", help="Outputs the number of homozygous samples for each loci", action="store_true")
zygosity_group.add_argument("--het", help="Outputs the number of heterozygous samples for each loci", action="store_true")
zygosity_group.add_argument("--unknown", help="Outputs the number of samples with unknown zygosity for each loci", action="store_true")
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
#				# Skip first column
#				if locus_name == "_a":
#					pass
#				else:
#					locus_names.append(locus_name)
				matrix_list.append(locus_name)
				dim1 = len(matrix_list)
			first_line = False
		# Subsequent lines contains the locus data from each individual.
		else:
			for x in line.split(","):
				matrix_list.append(x.rstrip())


	dim2 = int(len(matrix_list) / dim1)
	matrix = np.array(matrix_list).reshape(dim2, dim1)

	# Analyse the loci
	first_column = True
	for column in matrix.T:
		state = {"0":0, "1":0, "2":0}
		loci = None
		# Skip first column with sample names
		if first_column:
			first_column = False
			pass
		else:
			for x in column:
				if not loci:
					loci = x
				else:
					state[x] += 1

		if args.het and loci:
			print(loci, state["2"])
		elif args.hom and loci:
			print(loci, state["1"])
		elif args.unknown and loci:
			print(loci, state["0"])
			

			

if __name__ == "__main__":
    main()

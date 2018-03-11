#!/usr/bin/env python3

# Licence: 

# Usage:

import sys
import argparse

parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
parser.add_argument(dest="input_file", help="Input file")
parser.add_argument("--het_loci", help="Outputs the names of the heerozygous sites for each individual")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

class Individual(object):
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
		return self.het_states[locus_number]

	def __str__(self):
		return self.name


def main():
	
	data = open(args.input_file)
	individuals = []

	# Generate a list of Locus names
	# and subsequently store the data from
	# each individual in an object.
	first_line = True
	locus_names = []
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
#				if locus_name == " \n":
#					sufix = "_b"
				else:
					sufix = "_b"
				locus_name = name + sufix
				# Skip first column
				if locus_name == "_a":
					pass
				else:
					locus_names.append(locus_name)
			first_line = False
		else:
			# 'het' for heterozygosity state 
			individual = True
			het_states = []
			for het in line.split(","):
				if individual:
					individual_name = het
					individual = False
				else:
					het_states.append(het)
			# Store each individual in a list
			individuals.append(Individual(individual_name, locus_names, het_states))


	print(locus_names)
#	print(het_states)
#	for ind in individuals:
#		print(ind, ind.get_het_locus())
#	print(individuals)

#	locus_number = 0
#	for locus in locus_names:
#		print(locus)
#		state = individuals[locus_number].get_state(locus_number)
#		if int(state) == "2":
#			print(state)
#		locus_number += 1

if __name__ == "__main__":
    main()

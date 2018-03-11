#!/usr/bin/env python3

# Licence: 

# Usage:

import sys
import argparse

parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
parser.add_argument(dest="input_file", help="Input file")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

class Individual(object):
	def __init__(self, name):
		self.name = name

	def something(self):
		pass


def main():
	
	data = open(args.input_file)

	# Generate a list of Locus names
	# and subsequently store the data from
	# each individual in an object.
	first_line = True
	locus = []
	for line in data.readlines():
		if first_line:
			for locus_name in line.split(","):
				# Some locus names are inheriting its name from the previous column
				if locus_name != " ":
					name = locus_name
					sufix = "_a"
				else:
					name = name
					sufix = "_b"
				locus_name = name + sufix
				# Skip first columndd
				if locus_name == "_a":
					pass
				else:
					locus.append(locus_name)
			first_line = False
	print(locus)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Licence: 

# Usage:

import sys

parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

def main():

	data = open(sys.argv[1])

	for line in data.readlines():
		print(line)


if __name__ == "__main__":
    main()

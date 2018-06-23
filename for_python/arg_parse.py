
import argparse

parser = argparse.ArgumentParser(description = 'read the file in reverse order')
parser.add_argument('filename', help ='the file to read')
parser.add_argument('--limit', '-l',type = int , help = 'the number of lines to be read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
with open(args.filename) as f:
	lines = f.readlines()
	lines.reverse()
	
	if args.limit:
		lines = lines[:args.limit]
	for line in lines:
		print(line.strip()[::-1])
	

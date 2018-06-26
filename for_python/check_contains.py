import argparse

parser = argparse.ArgumentParser(description = 'This will search the pattern in the given specofic file')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')
args = parser.parse_args()
snippet = args.snippet.lower()

with open('names.txt') as f:
  words = f.readlines()

matches = []

for word in words:
   if snippet in word.lower():
       matches.append(word)

print([word.strip() for word in words if snippet in word.lower()])

print(matches)

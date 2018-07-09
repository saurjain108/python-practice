import re

pattern = r"Python"
sequence = "Python"
if re.match(pattern, sequence):
  print("Match is success!")
else: print("match is not success !")

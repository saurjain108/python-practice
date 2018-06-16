
import os

a = os.environ["PWD"]
b = os.environ["USER"]
c = os.environ["LOGNAME"]
d = os.environ["HOME"]
e = os.environ["OLDPWD"]

print(f"The current working directory is: {a}")
print(f"The current username is: {b}")
print(f"The current logname is: {c}")
print(f"The home location is: {d}")
print(f"The previous working directory is: {e}")


import re
str=input("Enter string: ")
if (re.search("^[a-zA-Z0-9]+$", str)):
  print("MATCHED")
else:
  print("NOT MATCHED")
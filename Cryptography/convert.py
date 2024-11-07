import sys
'''chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup1.index(char)
  out += lookup2[(cur - prev) % 40]
  prev = cur

sys.stdout.write(out)

for x in lookup1:
  if x == "h":
    print(lookup1.index("h"))
  elif x == " ":
    print("empty")
  else:
    print(x)

prev=0
chars = ""
out = "brHADM"
for char in out:
  cur =lookup2.index(char)
  if (cur-prev)>=0:
    chars += lookup1[cur-prev]
  else:
    chars += lookup1[40-char]'''

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

# Encoded string
encoded = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
decoded = ""
prev = 0

for char in encoded:
    # Find the current index of the character in lookup2
    cur = lookup2.index(char)
    
    # Reverse the encoding calculation to get the original index in lookup1
    original_index = (cur + prev) % 40
    
    # Append the character from lookup1 corresponding to original_index to decoded string
    decoded += lookup1[original_index]
    
    # Update prev for the next character
    prev = original_index

print(decoded)  # Should output "hello"

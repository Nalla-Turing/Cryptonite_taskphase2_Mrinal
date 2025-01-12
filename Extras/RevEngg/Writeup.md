# Extra challenges writeup for Reverse Engineering

## Transformation
Just needed to reverse the code in the question.
It was taking pair of character converting to ASCII, bitwise left shift firs one by 8 and add it in the ascii of the second code then converting it back to text.

## vault-door-training
The flag was in the code itself

## packer
Found the type of packing by taking out the strings and finding UPX! packer
Then decompress it using upx tool i found in there
Then took out the .text section and just guessed to find the flag string in the section header
The number i got, I converted it from hex ot ascii to get the flag

## FactCheck

## ClassicCrackme x100

## WinAntiDbg0x100

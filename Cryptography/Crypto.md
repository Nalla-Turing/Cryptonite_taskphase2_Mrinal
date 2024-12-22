# Crypto challenges
This writeup is to save the progress report of Cryptography challenges.

## Challenge-1 C3

process
Looki at the ciphering file, i convert a deiphering code as follows

    lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
    lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

    def find_cur(lhs, prev):
	    return (lhs + prev) % 40


    ciphertext = list("DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl")

    decrypted =  ""
    prev = 0

    for char in ciphertext:
	
	    lookup2_index = lookup2.index(char)
	    cur = find_cur(lookup2_index, prev)
	    decrypted += lookup1[cur]
	    prev = cur


    print(decrypted)

Now using this i got another piece of code
it is a python2 script which takes itself as the input
So i use wsl to input the file into the python file to get the flag
`Flag` `picoCTF{adlibs}`
<br>

### Things Learned

What is sys library in python

What is fileinput and what does it do

What does input do in the fileinput module
<br><br><br>

## Challenge-2 Custom encryption

### Process
The provided code is using a modified encryption method combining Diffie-Hellman key exchange, a XOR encryption, and a custom transformation.

First Diffie method is using to bring out a and b to make a shared_key
no since values of `a` `b` `g` `p` is known, we bring out the shared key using
    
    zebra1 = randint(p - 10, p)
    zebra2 = randint(g - 10, g)
    buffalo = al_qaeda(g, zebra1, p)
    giraffe1 = al_qaeda(g, zebra2, p)
    elephant = None
    if buffalo == giraffe1:
        elephant = buffalo
    else:
        print("Invalid key")

Then we use this as shared key to get our semi plan using

    def taliban(monkey, panda):
    koala = []
    for value in monkey:
        rabbit = value // (panda * 311)
        koala.append(chr(rabbit))
    return ''.join(koala)

And then we get our flag using

    def isis(parrot, dolphin):
    giraffe = ""
    key_length = len(dolphin)
    for i, kangaroo in enumerate(parrot):
        zebra = dolphin[i % key_length]
        cheetah = chr(ord(kangaroo) ^ ord(zebra))
        giraffe += cheetah
    return giraffe[::-1]

Thus the flag we get is

`picoCTF{custom_d2cr0pt6d_dc499538}`

### Things i learned 
Diffie-Hellman key exchange

### Problems I faced
Took too much time on understanding the logic of the programs
<br><br><br>

## Challenge-3 MiniRSA

### Process
Now we know that in RSA encryption we got our Message encrypted as `(Message^e)%n  = ciphertext`, thus all the headache will be to convert find i such that

`n*i + ciphertext = root(Message, e)`

Since N and ciphertext aren't that different in size, we can find bruteforce our way to find `i`

So check if n*i + ciphertext is the root of Message as I did in `rsasolution.py` 
or not using irootwhich also gives you the message
 now message to hex and then to ascii gives

`picoCTF{picoCTF{n33d_a_lArg3r_e_d0cd6eae}}`

### what i learned
RSA encryption method and it's variations
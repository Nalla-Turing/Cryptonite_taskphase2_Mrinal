# Crypto challenges
This writeup is to save the progress report of Cryptography challenges.

## Challenge-1 C3

### Flag
`Flag` `picoCTF{adlibs}`

<br>

### Steps Involved

<br>

### Things Learned

#### What is sys library in python

#### What is fileinput and what does it do

## Challenge-2 MiniRSA

### Process
Now we know that in RSA encryption we got our Message encrypted as `(Message^e)%n  = ciphertext`, thus all the headache will be to convert find i such that

`n*i + ciphertext = root(Message, e)`

Since N and ciphertext aren't that different in size, we can find bruteforce our way to find `i`

So check if n*i + ciphertext is the root of Message or not using irootwhich also gives you the message
 now message to hex and then to ascii gives

`picoCTF{picoCTF{n33d_a_lArg3r_e_d0cd6eae}}`
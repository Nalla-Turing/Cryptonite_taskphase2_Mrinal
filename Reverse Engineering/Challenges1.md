# Reverse Engineering challenge cryptonite TP2
This taskphase challenges focus the art of reverse engineering the source code of a given program.

## Challenge-1 GDB baby step 1

`Flag` `picoCTF{549698}`

### Steps to complete the challenge
1:- Trying to find information about the file
For that I used `file debugger0_a` to find all the necessary information about the file

    debugger0_a: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15a10290db2cd2ec0c123cf80b88ed7d7f5cf9ff, for GNU/Linux 3.2.0, not stripped

2:- Trying to learn about what is written here??
A lot of stuff I didn't fullyn understand but this `not-stripped` sounds important cause Chat Gpt

3:- What is Non Stripped?
It means our binary file retains information aout symbols that point to function, variables and sometimes debugging symbols.

4:- `gdb ./debugger0_a` to find more information
`no debugging symbols found` so it may contain function and variable symbols

5:- Using hint 2 i try ot find functions in gdb file using `info functions`

6: I see the main function

7:- disassemble main fucntion using `disassemble main`

8:- ''' Dump of assembler code for function main:
   0x0000555555555129 <+0>:     endbr64
   0x000055555555512d <+4>:     push   %rbp
   0x000055555555512e <+5>:     mov    %rsp,%rbp
=> 0x0000555555555131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000555555555134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000555555555138 <+15>:    mov    $0x86342,%eax
   0x000055555555513d <+20>:    pop    %rbp
   0x000055555555513e <+21>:    ret '''

9:- `0x86342` ius getting into eax register which is `549698` in decimal

### Things i learned while working on this challenge
First I would just like to add in the basic of reverse engineering I learned before attempting the challenge.

### What are registers? And their basics
Registers are used to store the most used memory material making it much faster to work  on the computer assembly, rather than getting our data from the main memory itself making mit much slower.

We use mutliple type of regsiters in our assembly language. Our file when searched through an exif tool is actually an `x86`  type archittecture so I will focus on learing the assembly for that type of computer architecture.

We have multiple type of registers depending on what we want to do:-

General-Purpose Registers
These are like multi-use spaces at your desk where you can hold any information you need right now, whether it’s a number, an address, or even a temporary result. Examples in x86 assembly:

`EAX`: Often used as an accumulator for arithmetic operations.
`EBX`: Often used to store base addresses for data in memory.
`ECX`: Commonly used as a counter in loops.
`EDX`: Used to hold data for input/output operations.

<br>

### User space, Kernel space and system calls
User space is the part in a CPU process where the cpu takes commands from the user to complete the fucntion but it doesn't have the right to acces the hardware that is doing the actual work.

For that CPU needs to turn into the kernel mode, which has all the required access. 

User mode sends a reuqest or a system call to the kernel mode to check if the request is valid and if the prcess can be done. IF the reuqirements are fulfilled, then the kernel mode will complete your process and give the desired output to the user space.


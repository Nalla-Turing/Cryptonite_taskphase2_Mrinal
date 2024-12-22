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

## Mistakes Made along the way???
1:- I tried to add break at main function and run the file to see what happens

2:- Tried to run the main function and check every step one by one using `step` command

3:- Wasted a lot of time to install ida free to disassemble this file

<br><br>

## Challenge-2 ARMssembly 1

`FLAG` `picoCTF{0000004D}`

### Steps Involved
1 I downloaded the file and saw it was a an ARMassembly `.s` file

2:-Went into youtube to learn a bit about ARM Assembly

3:- Saw that func is the starting point and it is doing some basic arithmatic operation, bitwise shift and storing. Which in the end gives `w0` the value of `w1` (which is 77 here) subtratcted by `value at sp+12`

4:- Now in the main function It again doing similar stuff with creating backward decreement stack with stack pointer back wounded by 48

5:- Then the main thing that branched to `.L0` label which is our win condition is that `w0` from `func` should be equal to 0.

6:- That means `w0` at `sp+12` must be equal to 77

7:- Converted 77 into hex to get `0x4D` this gives us the flag
<br>

### Things I learned along the way

#### What is ARM Assembly and basics of it
So ARM jsut like x86 is another type of assembly architecture that is written in text format with `.S` extension

In basic ARM assembly architecture we have multiple kind of registers
`r0`to `r6`
Which contains the first few arguments for our assembly code

`r7` Which contains the code for our system calls

`pc` counter which contains the address to the next step that will happen

#### What are directives? .global? .text? .align?
Directives are like additiona information about our assembly code which range from where our program should start  to what will be the format of our program etc

`.global` this directive make sure our intial point is available to other assembly files and not just the current ones

"It's like making your function available throughout all files"

`.text` this driective Specifies the start of a code section, where you write the actual instructions.

This section typically contains the program’s executable code.

`.align` Aligns data or code on specific memory boundaries, often to improve access speed.

#### WHat are sp and w0 registers??
`sp` is the stack pointer register which points to the top of a stack and is used to make space for more itema to be put in a stack

In ARM64 type the geenral purpose registers are from x0 to x30
Each of whom can contain 64 bits information
In `x0` register the lower part of 32 bits is contained in `w0` register
So `w0` is like the subpart of the bigger `x0` register

#### new commands that in learned
`str` stores value from `<base register>` into `[address]`

`ldr` loads value into `<base register>` from `[address]`

`ldl` bitwise shifts value in `<base register>` by value in `<address register>`

`sub sp,sp, #32` basically creates a 32 bit stack space for us to work in
we need to close this also at the end by doing `add sp,sp, 32`

`stp	x29, x30, [sp, -48]!` creates a backward decreement stack of 48
Then stores `x29` at `sp - 48` and `x30` at `sp - 40`
Then write-back the pointer to `x29`
So our sp starts at `original sp -48`

## Challenge-3 Vault door 3

### Process
Ok first we need to identify what the programm is doing

Well the code is taking in the password, extracting the password inside {} brackets

 Then 
 First 8 characters of password (password.charAt(i) where i is 0 to 7) are copied as-is.

Characters from index 8 to 15 are taken in reverse order from the range 8 to 15 in the password.

Characters from index 16 to 31 are constructed in a zigzag pattern.

So i just need to reverse engineer the code as I did in `solution.py` and viola we have the flag

`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}`
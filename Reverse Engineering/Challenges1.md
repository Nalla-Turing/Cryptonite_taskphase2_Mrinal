# Reverse Engineering challenge cryptonite TP2
This taskphase challenges focus the art of reverse engineering the source code of a given program.

## Challenge-1 GDB baby step 1

`Flag`

### Steps to complete the challenge


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


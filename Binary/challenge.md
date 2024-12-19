# Binary Exploitation
<br>

## Challenge-1 Buffer Overflow 0

### Process
Looking at the code we see that 

    void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
    }

thus our buffer can only be 16 characters long at a time.

So I just run the netcat instance ` nc saturn.picoctf.net 51447`
and give the input `aaaaaaaaaaaaaaaaaaaaaaaaaaaa`

and get the overflowed flag
`picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}`
<br>

### Things Learned
what is `#define`?
 It is used to define a preprocessor directive that is used to define macro in C.

what is `signal function`
This function is used to set the custom handler for different signal outputs in the program
In this challenge specifically we use it set the handler for `SIGSEGV` or `segmentation fault`

what is `setresgid(gid, gid, gid)`
This is used to set the effective id as our id. We do this so that we can get effective permissions to work with different files and programs
<br>

### Mistakes I made
I had to learn everything in the code as i didn't what is going on
<br><br>

## Challenge-2 format string 0

### Process
As i am observing the main function of the format-string-0.c file. I come acoss this 
    char choice1[BUFSIZE];
    scanf("%s", choice1);
    char *menu1[3] = {"Breakf@st_Burger", "Gr%114d_Cheese", "Bac0n_D3luxe"};
    if (!on_menu(choice1, menu1, 3)) {
        printf("%s", "There is no such burger yet!\n");
        fflush(stdout);
    } else {
        int count = printf(choice1);
        if (count > 2 * BUFSIZE) {
            serve_bob();
        } else {
            printf("%s\n%s\n",
                    "Patrick is still hungry!",
                    "Try to serve him something of larger size!");
            fflush(stdout);
<br>

### Things learned
<br>

### Mistakes I made
<br>
def reverse_password(output):
    sVar3 = len(output)  # Length of the output string
    rounds = 3  # Number of obfuscation rounds
    original = list(output)  # Start with the output string

    for round in range(rounds - 1, -1, -1):  # Reverse the 3 rounds
        for i_1 in range(sVar3):  # Process each character
            uVar1 = (i_1 % 0xff >> 1 & 0x55) + (i_1 % 0xff & 0x55)
            uVar1 = ((uVar1 >> 2) & 0x33) + (uVar1 & 0x33)
            temp_char = ord(original[i_1]) - ord('a')
            temp_char = (temp_char - ((uVar1 >> 4) + (uVar1 & 0xf))) % 26
            original[i_1] = chr(temp_char + ord('a'))

    return ''.join(original)

# Given output string
output = "kgxmwpbpuqtorzapjhfmebmccvwycyvewpxiheifvnuqsrgexl"
password = reverse_password(output)
print("Original password:", password)

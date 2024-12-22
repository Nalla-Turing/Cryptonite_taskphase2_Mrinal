def reverse_password(hardcoded):
    buffer = list(hardcoded)
    password = [''] * 32

    for i in range(8):
        password[i] = buffer[i]
    
    for i in range(8, 16):
        password[23 - i] = buffer[i]
    
    for i in range(16, 32, 2):
        password[46 - i] = buffer[i]
    
    for i in range(31, 16, -2):
        password[i] = buffer[i]

    return ''.join(password)

hardcoded = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"
decoded_password = reverse_password(hardcoded)
print("Decoded password:", decoded_password)

from random import randint

def al_qaeda(g, x, p):
    return pow(g, x) % p

def isis(parrot, dolphin):
    giraffe = ""
    key_length = len(dolphin)
    for i, kangaroo in enumerate(parrot):
        zebra = dolphin[i % key_length]
        cheetah = chr(ord(kangaroo) ^ ord(zebra))
        giraffe += cheetah
    return giraffe[::-1]

def taliban(monkey, panda):
    koala = []
    for value in monkey:
        rabbit = value // (panda * 311)
        koala.append(chr(rabbit))
    return ''.join(koala)

def al_shabaab(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    return v <= 1

def hezbollah(parrot, dolphin, a, b):
    p = 97 
    g = 31  
    if not al_shabaab(p) and not al_shabaab(g):
        print("Enter prime numbers")
        return
    zebra1 = randint(p - 10, p)
    zebra2 = randint(g - 10, g)
    buffalo = al_qaeda(g, zebra1, p)
    giraffe1 = al_qaeda(g, zebra2, p)
    elephant = None
    if buffalo == giraffe1:
        elephant = buffalo
    else:
        print("Invalid key")
        return
    semi_plain = taliban(parrot, elephant)
    original_plaintext = isis(semi_plain, dolphin)
    print(f'Original plaintext is: {original_plaintext}')

if __name__ == "__main__":
    cipher = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]
    dolphin_key = "trudeau"
    a = 89
    b = 27
    hezbollah(cipher, dolphin_key, a, b)

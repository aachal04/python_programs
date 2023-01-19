def invert_bits():
    #User input
    n = int(input("Enter the integer to invert bits: "))
    start = int(input("Enter the starting position: "))
    count = int(input("Enter the number of bits to invert: "))
    #create a mask with count number of bits set to 1, starting from start
    mask = (2 ** count - 1) << start
    #xor the number with the mask
    n = n ^ mask
    return n
inverted_bits = invert_bits()
print(inverted_bits)
def expand_hex(short_form):
    start = 0
    if short_form[0] == '-':
        start = 1
    end = len(short_form)
    expanded_form = ""
    i = start
    while i < end:
        if short_form[i] == '-':
            start = int(short_form[i - 1:i], 16) + 1
            end = int(short_form[i + 1:i + 2], 16)
            for num in range(start, end + 1):
                expanded_form += chr(num)
            i += 2
        else:
            expanded_form += short_form[i]
            i += 1
    return expanded_form

short_form = input("Enter the hexadecimal short form string: ")
expanded_form = expand_hex(short_form)
print("Expanded form:", expanded_form)

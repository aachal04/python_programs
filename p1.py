n=int(input("Enter The number:"))
def number_to_string(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    elif n < 1000:
        return ones[n // 100] + " hundred " + ('' if n % 100 == 0 else ' ' + number_to_string(n % 100))
    elif n < 1000000:
        return number_to_string(n // 1000) + " thousand " + ('' if n % 1000 == 0 else ' ' + number_to_string(n % 1000))
    else:
        return 'number out of range'
print(number_to_string(n))
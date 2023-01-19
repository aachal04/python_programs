# Assign the range of characters



#first_char_start = input("Enter the first character:")
#last_char = input("Enter the last character:")
#str=input("Enter the Expression you want:")
#list1=[]
#list1[:0]=str
#print(list1)
#l=len(list1)

# Generate a list of assigned characters (here from 'a' to 'n')
#if (list1[0]!=45):
 #   for i in list1:
  #      if (range(len(list1))==45):
   #         start = list1.index(list1[-1])-1
    #        end = list1.index(list1[-1])+1
     #       alpha_list = [chr(i) for i in range(ord(start), ord(end) + 1)]

# Print a-n with spaces: a b c d e f g h i j k l m n
#print(" ".join(alpha_list))

# Every second in a-n: a c e g i k m
#print(" ".join(alpha_list[::2]))

# Append a-n to index of urls{hello.com/, hej.com/, ..., hallo.com/}
# Ex.hello.com/a hej.com/b ... hallo.com/n

#urls: list of urls
#results = [i+j for i,j in zip(alpha_list)]

#print new url list 'results' (concatenated two lists element-wise)
#print(results)
def last(l1):
     i = ord(l1[-1])
     if i != 45:
          string = ""
          for ele in l1:
               string+=ele
          print(string)
     else:
          l1.remove(l1[-1])
          checkfirst(l1)

def checkfirst(str1):
     l1 = []
     l1[:0] = str1
     i = ord(l1[0])
     if i != 45:
          last(l1)
     else:
          l1.remove(l1[0])
          checkfirst(l1)

"""def expand_string(short_norm):
    expanded_string = ""
    for x in short_norm.split("-"):
        if len(x) == 1:
            expanded_string += x
        else:
            v = 0
            start = ord(x[v])
            end = ord(x[v+1])
            expanded_string += "".join([chr(i) for i in range(start, end+1)])
    return expanded_string
"""
checkfirst("a-g")
checkfirst("b-h4-8") 
checkfirst("-c-e-") 


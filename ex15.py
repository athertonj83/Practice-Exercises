#ex15 reversing word order

def reversewords(string_input):
    print(string_input)
    new_string = " ".join(string_input.split()[::-1])
    print(new_string)
    
reversewords("hello from jennifer atherton")

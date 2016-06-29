#ex06 palindrome

#a string is a list!!!!!

while True:
    str_in=input("Please enter a string:")
    if not str_in.isalpha():
        continue
    else:
        break

str_in_reverse=str_in[::-1]
if str_in==str_in_reverse:
    print("These are the same - this is a palindrome")
else:
    print("These are not the same")




#ex 07 (doesn't require a new program - simple)
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# using lambda filter
for x in a:
    b=list(filter(lambda x: x%2==0, a))
print(b)

#or using list comprehension

for y in a:
    c=[y for y in a if y%2==0]
print(c)

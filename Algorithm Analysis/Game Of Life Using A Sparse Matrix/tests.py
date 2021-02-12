

num = 12
factorial = 1

for number in range( num ) :
    if num == 1 :
        break
    else :
        factorial *= num
        num -= 1

# Convert the factorial to a list of strings.
factorial = list( str(factorial ) )
print( factorial[::-1] )

# Iterate through the factorial from the last element
# keeping track of the zeros. 
count = 0
for val in factorial[::-1] :
    if val == '0' :
        count += 1

    else :
        break

print( count )

# output.
# 2

a = "Mike"
b = "Allan"

a, b = b, a
print(a)
print(b)

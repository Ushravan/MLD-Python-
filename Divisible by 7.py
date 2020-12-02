# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200.The numbers obtained should be printed in a comma-separated sequence on a single line.

nl=[]

for n in range(2000, 6200):
    if (n%7==0) and (n%5!=0):
        nl.append(str(n))
print (','.join(nl))


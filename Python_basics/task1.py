# script to create list of 100 random numbers from 0 to 1000:
import random
a = []
for i in range(101):
    a.append(random.randint(0, 1000))
print(a)

# script to sort list from min to max (without using sort())
b = []
while a:
    min_value = min(a)
    b.append(min_value)
    a.remove(min_value)
print(b)

#calculate average for even and odd numbers
c = []
d = []
for i in b:
    if i%2 == 0:
        c.append(i)
    else:
        d.append(i)
print(sum(c)/len(c))
print(sum(d)/len(d))
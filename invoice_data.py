# #Data setting for invoice , Can be generated from Database or Excel ##
from datetime import date
today = date.today()
print(today)
# import module
l=[10,20,30,40]
for i in l:
    import random as r
    ph_no = []
    ph_no.append(r.randint(6, 9))

# the first number should be in the range of 6 to 9


# the for loop is used to append the other 9 numbers.
# the other 9 numbers can be in the range of 0 to 9.
for i in range(1, 10):
	ph_no.append(r.randint(0, 9))

# printing the number
for i in ph_no:
    print(i)
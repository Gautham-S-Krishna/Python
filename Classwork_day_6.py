# Question 1
count = 0
total = 0
attendance = [18,20,19,15,21]
for x in attendance:
    if x >= 20:
        print(x,'Full')
        count=count+1
    else:
        print(x,'not full')
    total=total+x       
# To count how many are full and total number
print(count)
print(total)

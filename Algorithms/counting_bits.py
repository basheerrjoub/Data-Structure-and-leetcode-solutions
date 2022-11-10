
n = 2
def num_of_ones(num):
    sum = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            sum+=1
            num -=1
    return sum


rList = []
for num in range(n+1):
    rList.append(num_of_ones(num))
print (rList)




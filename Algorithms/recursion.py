
def count_down(number):
    if(number == 0):
        return;
    else:
        number -= 1
        count_down(number)
        print (number)



def factorial(number):
    if number == 1:
        return 1;
    else:
        return number * factorial(number - 1)



#######################################################################################
##                                                                                   ##
##  tail recursion is better regarding the use of the stack residing in the memory.. ##
##                                                                                   ##
#######################################################################################
#Normal Recursion
def sum(number):
    if number == 0:
        return 0;
    else:
        return number + sum(number-1)

#tail Recursion
def sum_tail(number, total=0):
    if number == 0:
        return total;
    else:
        return sum_tail(number-1, total + number)


# Recursive functions

def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n -1)

'''The reason this works is ... well let's first break down the code and see what is essentially happening
so what is happening we take in an argument n which represents the number that the user wants to take the factorial of
then from there what we essentially do is that we say if the user passes in 1 which we know that the factorial of 1 is 1 therefore we can
return 1 but if that is not the case then we want to take the number the user passes in and we want to multiply
that number to every number decremented by one and we know this would be save due to the simple fact that we have a base case saying 
that if it reaches 1 we can return out '''

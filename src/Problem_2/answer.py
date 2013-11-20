'''
My answer to project euler question 2.
'''

_DEBUG = False

def debug_print(message):
    '''
    Simple debug log
    '''
    if _DEBUG:
        print "DEBUG>>> {0}".format(message)


def main():
    '''
    The function that is run when opening this file
    '''

    print "And the answer is: {0}".format(fib(4000000))


def fib(limit):
    '''
    perform fiboracci
    '''
    fib1 = 1
    fib2 = 0
    result = 0

    summed = 0
    while result < limit:
        debug_print("{0}, {1} - Total: {2} ".format(fib2, fib1, summed))

        if is_even(fib1):
            summed = summed + fib1

        result = fib1 + fib2
        fib2 = fib1
        fib1 = result

    return summed


def is_even(num):
    '''
    Wrapper to hide details about module function
    '''
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
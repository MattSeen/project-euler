'''
    My attempt at Problem 4. This provides the right answer, however it is quite
    slow for what it is doing and I would like to know how I can go about 
    speeding it up.
'''

def is_palindromic(num):
    '''
        Test if a number is palindromic,
        Essentially a string test... probably a performance bottle neck.

        Alterative mathematical implementation
    '''
    test_value = abs(num)

    if(test_value < 10):
        return True

    # temp = str(test_value)
    # return (temp == temp[::-1])

    num = test_value
    reverse = 0
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num / 10
    return (test_value == reverse)


def get_largest_palindrom(range_start, range_end):
    '''
        Something goes here.
    '''
    if range_start > range_end:
        return -1


    largest_num = 0
    for outer in xrange(range_start, range_end):
        for inner in xrange(range_start, range_end):
            num = outer * inner

            if is_palindromic(num):
                if largest_num < num:
                    largest_num = num

    return largest_num


def main():
    '''
        Entry point.
    '''
    answer = get_largest_palindrom(100, 999)
    print answer

if __name__ == '__main__':
    main()

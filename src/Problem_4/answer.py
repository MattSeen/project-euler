'''
    My attempt at Problem 4. This provides the right answer, however it is quite
    slow for what it is doing and I would like to know how I can go about 
    speeding it up.
'''

def is_palindromic(num):
    '''
        Test if a number is palindromic,
        Essentially a string test... probably a performance bottle neck.
    '''
    if(abs(num) < 10):
        return True

    temp = str(abs(num))

    return (temp == temp[::-1])

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

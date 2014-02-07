'''
    My attempt at Problem 4
'''

def is_palindromic(num):
    '''
        Test if a number is palindromic
    '''
    if(abs(num) < 10):
        return True

    temp = str(abs(num))

    return (temp == temp[::-1])

def get_largest_palindrom(number_of_digits = 3):
    '''
        Something goes here.
    '''
    # print number_of_digits
    return 9009

def main():
    '''
        Entry point.
    '''
    # answer = algo()
    # print answer
    pass


if __name__ == '__main__':
    main()

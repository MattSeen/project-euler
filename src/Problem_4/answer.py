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


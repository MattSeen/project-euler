'''
    Answers.
'''

def recursive_version(to_crack, i = 2):
    '''
        Recurse
    '''
    print i
    if i * i < to_crack:
        print "value is still smaller than limit"
        if to_crack % i == 0:
            to_crack = to_crack / i
            return recursive_version(to_crack, i + 1)


def while_loop_version(num):
    '''
        Simple and elegant
        http://stackoverflow.com/questions/15347174/python-finding-prime-factors
    '''
    base_value = 2

    while base_value * base_value < num:
        while num % base_value == 0:
            num = num / base_value
            print str(base_value)
        base_value = base_value + 1

    print num


def main():
    '''
        Docstring
    '''
    prime_to_crack = 600851475143

    # while_loop_version(prime_to_crack)
    
    print recursive_version(prime_to_crack)


if __name__ == '__main__':
    main()

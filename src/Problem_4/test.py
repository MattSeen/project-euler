'''
    Test are a series of tests for my answer to problem 4 of the project euler
    website.
'''

from nose.tools import assert_equals
import answer

def test_is_palindromic():
    '''
        Test my function to inspect whether a number is palindromic.
        Negative and positive cases.
    '''
    assert_equals(answer.is_palindromic(1), True)
    assert_equals(answer.is_palindromic(9000), False)
    assert_equals(answer.is_palindromic(9009), True)

    assert_equals(answer.is_palindromic(-1001), True)
    assert_equals(answer.is_palindromic(1001.98898), False)

def test_get_largest_palindrom():
    '''
        My function to get the largest palindrom is quite restrictive and only 
        takes two digits.
        Ensure the output of this is at least correct.
    '''
    assert_equals(answer.get_largest_palindrom(100, 99), -1)
    
    assert_equals(answer.get_largest_palindrom(1, 100), 9009)
    assert answer.is_palindromic(answer.get_largest_palindrom(1, 100))

    two_digit = answer.get_largest_palindrom(10, 100)
    three_digit = answer.get_largest_palindrom(100, 1000)

    assert two_digit != three_digit

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


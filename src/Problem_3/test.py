from nose.tools import assert_equals
import answer

def test_silly_method():
	assert_equals(answer.silly_method(), True)

def test_while_loop():
	
	assert_equals(answer.while_loop_version(1), 1)
	assert_equals(answer.while_loop_version(12), 3)
	assert_equals(answer.while_loop_version(12), 2)
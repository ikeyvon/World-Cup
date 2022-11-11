from unittest.mock import patch
from unittest import TestCase


def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


# class Test(TestCase):

#     # get_input will return 'yes' during this test
#     @patch('skratch2.get_input', return_value='yes')
#     def test_answer_yes(self, input):
#         self.assertEqual(answer(), 'you entered yes')    
#         print('test passed')

#     @patch('skratch2.get_input', return_value='no')
#     def test_answer_no(self, input):
#         self.assertEqual(answer(), 'you entered no')
#         print('test passed')

# Test().test_answer_yes()
# Test().test_answer_no()
exit()
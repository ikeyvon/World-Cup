from worldcup import *
from unittest.mock import patch
from unittest import TestCase
# .  

def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('worldcup.play', return_value= [2, 3])
    def test_wc_firstgame(self, input):
        # self.assertEqual(answer(), 'you entered yes')
        main()

Test().test_wc_firstgame()
exit()
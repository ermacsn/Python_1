from unittest import TestCase
from task import digits_sum

class TestHome(TestCase):
    def test_task(self):
        self.assertEqual(digits_sum(123), 6, msg='что то пошло не так')
 #       self.assertEqual(digits_sum(53), 8, msg='что-то пошло не так')
        self.assertNotEqual(digits_sum(53), 8, msg='не так')
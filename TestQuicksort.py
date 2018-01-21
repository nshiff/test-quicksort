from unittest import TestCase
from Quicksort import Quicksort



class TestQuicksort(TestCase):

    def setUp(self):
        self.qs = Quicksort()


    def test_trivial_sort(self):
        baby_list = [42]
        self.assertEqual(baby_list, self.qs.sort(baby_list))



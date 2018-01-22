from unittest import TestCase
from Quicksort import Quicksort



class TestQuicksort(TestCase):

    def setUp(self):
        self.qs = Quicksort()


    def test_trivial_sort(self):
        baby_list = [42]
        self.assertEqual(baby_list, self.qs.sort(baby_list))

    def test_get_pivot_subscript(self):
        list1 = [42]
        list2 = [7, 9, 6, 4, 4, 2, 6, 7, 3, 4]
        list3 = [2, 1, 3, 5]
        self.assertEqual(0, self.qs.get_pivot_subscript(list1))
        self.assertEqual(9, self.qs.get_pivot_subscript(list2))
        self.assertEqual(3, self.qs.get_pivot_subscript(list3))



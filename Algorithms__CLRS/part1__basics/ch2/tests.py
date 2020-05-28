import unittest
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.array_1 = list(range(20))
        self.array_2 = []
        self.array_3 = [4]
        self.array_4 = list(range(4, 30, 3))
        self.array_5 = [1, 1, 1, 1, 3, 3, 3, 4, 4, 0, 0, 0]
        self.array_6 = list(range(20))
        self.array_7 = list(range(-10, 10))

        self.sorted_array_1 = self.array_1[:]
        self.sorted_array_2 = self.array_2[:]
        self.sorted_array_3 = self.array_3[:]
        self.sorted_array_4 = self.array_4[:]
        self.sorted_array_5 = sorted(self.array_5[:])
        self.sorted_array_6 = self.array_6[:]
        self.sorted_array_7 = sorted(self.array_7[:])
        
        random.shuffle(self.array_1)
        random.shuffle(self.array_4)  
        random.shuffle(self.array_5)     
        random.shuffle(self.array_7)

        self.arrays = [
            self.array_1, self.array_2, self.array_3, self.array_4,
            self.array_5, self.array_6, self.array_7,
        ]
        self.sorted_arrays = [
            self.sorted_array_1, self.sorted_array_2, self.sorted_array_3,
            self.sorted_array_4, self.sorted_array_5, self.sorted_array_6,
            self.sorted_array_7,
        ]

    def sort_arrays(self, sorting_func):
        for array in self.arrays:
            sorting_func(array)

    def check_sorting(self):
        for i in range(len(self.arrays)):
            self.assertEqual(
                self.arrays[i], self.sorted_arrays[i],
            )

    def test_insertion_sort(self):
        self.sort_arrays(insertion_sort)
        self.check_sorting()
        
    def test_merge_sort(self):
        self.sort_arrays(merge_sort)
        self.check_sorting()

    def test_selection_sort(self):
        self.sort_arrays(selection_sort)
        self.check_sorting()


if __name__ == "__main__":
    unittest.main()

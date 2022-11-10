from unittest import TestCase

import task4

class Test(TestCase):
    def test_rle_compress(self):
        input = "ССССъешьььь ееееещё этииииииих #_1а мяягких фффранцузских булок, да выпей же чаю #1а аааа"
        actual = task4.rle_compress(input)
        expected = "#4Съеш#4ь #5ещё эт#7их #__1а мяягких фффранцузских булок, да выпей же чаю #_1а #4а"
        self.assertEqual(expected, actual)

    def test_rle_decompress(self):
        input = "#4Съеш#4ь #5ещё эт#7их #__1а мяягких фффранцузских булок, да выпей же чаю #_1а #4а"
        actual = task4.rle_decompress(input)
        expected = "ССССъешьььь ееееещё этииииииих #_1а мяягких фффранцузских булок, да выпей же чаю #1а аааа"
        self.assertEqual(expected, actual)

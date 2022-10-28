from unittest import TestCase

import task4

class Test(TestCase):
    def test_rele_compress(self):
        input = "ССССъешьььь ееееещё этииииииих мяягких фффранцузских булок, да выпей же чаю #1а"
        actual = task4.rle_compress(input)
        expected = "#4Съеш#4ь #5ещё эт#7их мяягких фффранцузских булок, да выпей же чаю #_1а"
        self.assertEqual(expected, actual)

    def test_rle_decompress(self):
        input = "Съеш#4ь #5ещё эт#7их мяягких фффранцузских булок, да выпей же чаю #_1а"
        actual = task4.rle_decompress(input)
        expected = "Съешьььь ееееещё этииииииих мяягких фффранцузских булок, да выпей же чаю #1а"
        self.assertEqual(expected, actual)

from unittest import TestCase

import task4

class Test(TestCase):
    def test_rele_compress(self):
        input = "Съешьььь   ееееещё этииииииих мяягких фффранцузских булок, да выпей же чаю а4"
        actual = task4.rle_compress(input)
        expected = "Съешь4 3е5щё эти7х мяягких ф3ранцузских булок, да выпей же чаю а!4"
        self.assertEqual(actual, expected)

    #def test_rle_decompress(self):
    #    input = "Съешь ещё этих мягких французских булок, дабва абввыпейабв жеабв абвчаю"
    #    actual = task1.remove_abv_words(input)
    #    expected = "Съешь ещё этих мягких французских булок,"
    #    self.fail()

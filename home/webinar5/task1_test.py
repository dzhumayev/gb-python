from unittest import TestCase

import task1

class Test(TestCase):
    def test_remove_abv_words(self):
        input = "Съешь ещё этих мягких французских булок, дабва абввыпейабв жеабв абвчаю"
        actual = task1.remove_abv_words(input)
        expected = "Съешь ещё этих мягких французских булок,"
        self.assertEqual(actual, expected)

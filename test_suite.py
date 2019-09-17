import unittest
import driver

class TestSuite(unittest.TestCase):
    def test_word_was_guessed(self):
        word_set = set('microbiome')
        guessed_words_set = set('essdfmrnsdfjhkcviurbtiuiuxoyiupiqmnzx')
        self.assertTrue(driver.is_word_guessed(word_set, guessed_words_set))

    def test_word_not_guessed(self):
        word_set = set('microbiome')
        guessed_words_set = set('asdfghjtry')
        self.assertFalse(driver.is_word_guessed(word_set, guessed_words_set))

    def test_guess_in_word(self):
        guess = 'm'
        word_set = set('microbiome')
        self.assertTrue(driver.is_guess_in_word(guess, word_set))

    def test_guess_not_in_word(self):
        guess = 'j'
        word_set = set('microbiome')
        self.assertFalse(driver.is_guess_in_word(guess, word_set))

if __name__ == '__main__':
    unittest.main()

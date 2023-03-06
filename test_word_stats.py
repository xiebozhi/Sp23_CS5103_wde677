import unittest
from word_stats import count_words  # Import the count_words function from the word_stats module


class TestCountWords(unittest.TestCase):
    def test_normal_input(self):
        doc = "This is a test. This is only a test."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 1, 'only': 1, 'test': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_special_characters(self):
        doc = "The quick brown fox jumps over the lazy dog."
        expected_output = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog.': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_case_insensitive(self):
        doc = "Hello, World! This is a TEST of case-insensitive words."
        expected_output = {'hello,': 1, 'world!': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1, 'of': 1, 'case-insensitive': 1, 'words.': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_empty_input(self):
        doc = ""
        with self.assertRaises(ValueError):
            count_words(doc)

    def test_maximum_length(self):
        doc = "A" * 10001
        with self.assertRaises(ValueError):
            count_words(doc)

    def test_newline_characters(self):
        doc = "This is a test.\nThis is only a test.\n"
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 1, 'only': 1, 'test': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_tab_characters(self):
        doc = "This\tis\ta\ttest.\tThis\tis\tonly\ta\ttest."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 1, 'only': 1, 'test': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_combination_of_separators(self):
        doc = "This \tis\n a\t test.\nThis\tis only a test."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 1, 'only': 1, 'test': 1}
        self.assertEqual(count_words(doc), expected_output)

if __name__ == '__main__':
    unittest.main()
# Bobb Shields
# wde677
#

# Unit testing code for word statistics functions
# First sprint: count_words
# Second sprint: count_lines, count_chars
#


import unittest
from word_stats import count_words  # Import the count_words function from the word_stats module
from word_stats import count_lines
from word_stats import count_chars  

# Input checking Test Code
#
class TestInputChecking(unittest.TestCase):
    def test_empty_input(self):
        doc = ""
        with self.assertRaises(ValueError):
            count_words(doc)

    def test_maximum_length(self):
        doc = "A" * 10001
        with self.assertRaises(ValueError):
            count_words(doc)

# Word Count Test Code
#
class TestCountWords(unittest.TestCase):
    def test_normal_input(self):
        doc = "This is a test. This is only a test."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_case_insensitive(self):
        doc = "Hello, World! This is a TEST of case-insensitive words."
        expected_output = {'hello,': 1, 'world!': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1, 'of': 1, 'case-insensitive': 1, 'words.': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_newline_characters(self):
        doc = "This is a test.\nThis is only a test.\n"
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1, '': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_tab_characters(self):
        doc = "This\tis\ta\ttest.\tThis\tis\tonly\ta\ttest."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_combination_of_separators(self):
        doc = "This \tis\n a\t test.\nThis\tis only a test."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1, '': 3}
        self.assertEqual(count_words(doc), expected_output)

    def test_double_space(self):
        doc = "This  \tis\n a\t  test.\nThis\tis only a  test."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1, '': 6}
        self.assertEqual(count_words(doc), expected_output)

if __name__ == '__main__':
    unittest.main()

# Line Count Test Code
#
class TestCountLines(unittest.TestCase):
    def test_normal_input(self):
        doc = "This is a test. \nThis is only a test.\n"
        expected_output = 3
        self.assertEqual(count_lines(doc), expected_output)

# Char Count Test Code
#
class TestCountChars(unittest.TestCase):
    def test_normal_input(self):
        doc = "This is a test. \nThis is only a test.\n"
        expected_output = 28
        self.assertEqual(count_chars(doc), expected_output)

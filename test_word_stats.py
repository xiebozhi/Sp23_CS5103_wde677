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
from word_stats import check_input 
from word_stats import replace_word 
from word_stats import print_stats

#not sure what this is but afraid to delete it since unittest.(RELATED)
if __name__ == '__main__':
    unittest.main()

# Input checking Test Code
#
class TestInputChecking(unittest.TestCase):
    def test_empty_input(self):
        doc = ""
        with self.assertRaisesRegex(ValueError, "Input cannot be empty"):
            count_words(doc)

    def test_maximum_length(self): #User case: Data Scientist max limit concerns
        doc = "A" * 10001
        with self.assertRaisesRegex(ValueError, "Input exceeds maximum length"):
            count_lines(doc)

    def test_almost_maximum_length(self): #User case: Data Scientist max limit concerns
        doc = "A" * 10000
        self.assertTrue(check_input(doc))
    
    def test_is_string(self): 
        doc = 1000
        with self.assertRaisesRegex(TypeError, "Input must be a string"):
            check_input(doc)
    
    def test_good_list(self): 
        doc = ["test","test2"]
        self.assertTrue(check_input(doc))

    def test_null_list(self): 
        doc = ["","test2"]
        with self.assertRaisesRegex(TypeError, "Input cannot be empty"):
            check_input(doc)

# Word Count Test Code
#
class TestCountWords(unittest.TestCase):
    def test_normal_input(self):
        doc = "The quick brown fox jumped over the lazy dog, but the 1 dog didn't care. The fox was too fast for the 2 dogs to catch, and they could only watch as it disappeared into the distance. However, the 3rd dog was smarter than the others and knew a shortcut;\n\n it ran ahead and caught the fox by surprise! \"What's going on here?\" the fox asked. But the dog just barked in triumph, knowing that it had won the race.\n\n Meanwhile, the lazy dog snoozed on, oblivious to the excitement happening around it.\n + = % $ \n\n fin fin."        
        expected_output = {'the': 14, 'quick': 1, 'brown': 1, 'fox': 4, 'jumped': 1, 'over': 1, 'lazy': 2, 'dog,': 1, 'but': 2, '1': 1, 'dog': 4, "didn't": 1, 'care.': 1, 'was': 2, 'too': 1, 'fast': 1, 'for': 1, '2': 1, 'dogs': 1, 'to': 2, 'catch,': 1, 'and': 3, 'they': 1, 'could': 1, 'only': 1, 'watch': 1, 'as': 1, 'it': 3, 'disappeared': 1, 'into': 1, 'distance.': 1, 'however,': 1, '3rd': 1, 'smarter': 1, 'than': 1, 'others': 1, 'knew': 1, 'a': 1, 'shortcut;': 1, '': 8, 'ran': 1, 'ahead': 1, 'caught': 1, 'by': 1, 'surprise!': 1, '"what\'s': 1, 'going': 1, 'on': 1, 'here?"': 1, 'asked.': 1, 'just': 1, 'barked': 1, 'in': 1, 'triumph,': 1, 'knowing': 1, 'that': 1, 'had': 1, 'won': 1, 'race.': 1, 'meanwhile,': 1, 'snoozed': 1, 'on,': 1, 'oblivious': 1, 'excitement': 1, 'happening': 1, 'around': 1, 'it.': 1, '+': 1, '=': 1, '%': 1, '$': 1, 'fin': 1, 'fin.': 1}
        self.assertEqual(count_words(doc), expected_output)

    def test_case_insensitive(self):
        doc = "Hello, World! This is a TEST of case-insensitive words. Test test TESt Test"
        expected_output = {'hello,': 1, 'world!': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 5, 'of': 1, 'case-insensitive': 1, 'words.': 1}
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

# Line Count Test Code
#
class TestCountLines(unittest.TestCase):
    def test_normal_input(self):
        doc = "The quick brown fox jumped over the lazy dog, but the 1 dog didn't care. The fox was too fast for the 2 dogs to catch, and they could only watch as it disappeared into the distance. However, the 3rd dog was smarter than the others and knew a shortcut;\n\n it ran ahead and caught the fox by surprise! \"What's going on here?\" the fox asked. But the dog just barked in triumph, knowing that it had won the race.\n\n Meanwhile, the lazy dog snoozed on, oblivious to the excitement happening around it.\n + = % $ \n\n fin fin."        
        expected_output = 8
        self.assertEqual(count_lines(doc), expected_output)

    def test_tab_characters(self):
        doc = "This\tis\ta\ttest.\tThis\tis\tonly\ta\ttest."
        expected_output = 1
        self.assertEqual(count_lines(doc), expected_output)

    def test_combination_of_separators(self):
        doc = "This \tis\n a\t test.\nThis\tis only a test."
        expected_output = 3
        self.assertEqual(count_lines(doc), expected_output)

    def test_double_space(self):
        doc = "This  \tis\n a\t  test.\nThis\tis only a  test."
        expected_output = 3
        self.assertEqual(count_lines(doc), expected_output)

# Char Count Test Code
#
class TestCountChars(unittest.TestCase):
    def test_normal_input(self):
        doc = "The quick brown fox jumped over the lazy dog, but the 1 dog didn't care. The fox was too fast for the 2 dogs to catch, and they could only watch as it disappeared into the distance. However, the 3rd dog was smarter than the others and knew a shortcut;\n\n it ran ahead and caught the fox by surprise! \"What's going on here?\" the fox asked. But the dog just barked in triumph, knowing that it had won the race.\n\n Meanwhile, the lazy dog snoozed on, oblivious to the excitement happening around it.\n + = % $ \n\n fin fin."        
        expected_output = 409
        self.assertEqual(count_chars(doc), expected_output)
    def test_tab_characters(self):
        doc = "This\tis\ta\ttest.\tThis\tis\tonly\ta\ttest."
        expected_output = 28
        self.assertEqual(count_chars(doc), expected_output)

    def test_combination_of_separators(self):
        doc = "This \tis\n a\t test.\nThis\tis only a test."
        expected_output = 28
        self.assertEqual(count_chars(doc), expected_output)

    def test_double_space(self):
        doc = "This  \tis\n a\t  test.\nThis\tis only a  test."
        expected_output = 28
        self.assertEqual(count_chars(doc), expected_output)

# Scenario print_stats Test Code
#
class TestScenarios(unittest.TestCase):
    def test_NumbersWithTabs(self):
        doc = "1\t2\t3\t4\n5\t6\t7\t8\n9\t10\t11\t12"
        try:
            print(print_stats(doc))
        except:
            self.fail("Unexpected exception was raised.")

    def test_simple_formula(self):
        doc = "30 = [(2 + 4) * (8 / 2)] - 10 + 5^2 * (3 - 1) / 4"
        try:
            print(print_stats(doc))
        except:
            self.fail("Unexpected exception was raised.")

    def test_normal_insert(self):
        doc = "The quick brown fox jumped over the lazy dog, but the 1 dog didn't care. The fox was too fast for the 2 dogs to catch, and they could only watch as it disappeared into the distance. However, the 3rd dog was smarter than the others and knew a shortcut;\n\n it ran ahead and caught the fox by surprise! \"What's going on here?\" the fox asked. But the dog just barked in triumph, knowing that it had won the race.\n\n Meanwhile, the lazy dog snoozed on, oblivious to the excitement happening around it.\n + = % $ \n\n fin fin."        
        try:
            print(print_stats(doc))
        except:
            self.fail("Unexpected exception was raised.")                  

# Replace Word Test Code
# 
class TestWordReplace(unittest.TestCase):
    def test_replace_normal(self):
        doc = "The quick brown fox jumped over the lazy dog, but the 1 dog didn't care. The fox was too fast for the 2 dogs to catch, and they could only watch as it disappeared into the distance. However, the 3rd dog was smarter than the others and knew a shortcut;\n\n it ran ahead and caught the fox by surprise! \"What's going on here?\" the fox asked. But the dog just barked in triumph, knowing that it had won the race.\n\n Meanwhile, the lazy dog snoozed on, oblivious to the excitement happening around it.\n + = % $ \n\n fin fin."        
        expected_output = "The quick brown fox jumped over THE lazy dog, but THE 1 dog didn't care. The fox was too fast for THE 2 dogs to catch, and THEy could only watch as it disappeared into THE distance. However, THE 3rd dog was smarter than THE oTHErs and knew a shortcut;\n\n it ran ahead and caught THE fox by surprise! \"What's going on here?\" THE fox asked. But THE dog just barked in triumph, knowing that it had won THE race.\n\n Meanwhile, THE lazy dog snoozed on, oblivious to THE excitement happening around it.\n + = % $ \n\n fin fin."        
        self.assertEqual(replace_word(doc,"the", "THE"), expected_output)

    def test_distinct_words_1(self):
        doc = "The the THE thee three"
        expected_output = "FFF the THE thee three"
        self.assertEqual(replace_word(doc, "The", "FFF"), expected_output)

    def test_distinct_words_2(self):
        doc = "The the THE thee three"
        expected_output = "The FFF THE thee three"
        self.assertEqual(replace_word(doc, "the", "FFF"), expected_output)

    def test_distinct_words_3(self):
        doc = "The the THE thee three"
        expected_output = "The the FFF thee three"
        self.assertEqual(replace_word(doc, "THE", "FFF"), expected_output)

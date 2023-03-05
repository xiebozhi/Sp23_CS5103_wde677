def test_count_words():
    # Test case 1
    doc1 = "The quick brown fox jumps over the lazy dog."
    expected_output1 = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog.': 1}
    assert count_words(doc1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, but got {count_words(doc1)}"

    # Test case 2
    doc2 = "The cat in the hat\nsat on the mat."
    expected_output2 = {'the': 2, 'cat': 1, 'in': 1, 'hat': 1, 'sat': 1, 'on': 1, 'mat.': 1}
    assert count_words(doc2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, but got {count_words(doc2)}"

    # Test case 3
    doc3 = "To be or not to be, that is the question.To be or not to be, that is the question!To be or not to be, that is the question?"
    expected_output3 = {'to': 6, 'be': 6, 'or': 3, 'not': 3, 'that': 3, 'is': 3, 'the': 3, 'question.': 3}
    assert count_words(doc3) == expected_output3, f"Test case 3 failed: expected {expected_output3}, but got {count_words(doc3)}"

    # Test case 4
    doc4 = ""
    expected_output4 = {'' : 1}
    assert count_words(doc4) == expected_output4, f"Test case 4 failed: expected {expected_output4}, but got {count_words(doc4)}"
    
    # Test case 5
    doc5 = "hello world\nhello world\nHello WORLD"
    expected_output5 = {'hello': 3, 'world': 3}
    assert count_words(doc5) == expected_output5, f"Test case 5 failed: expected {expected_output5}, but got {count_words(doc5)}"
    
    print("All test cases passed!")

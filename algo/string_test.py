"""
Unit test file for the string library string.py

G. Platonov
7/15/2022
"""

from string import *

substr_search_tests = [
    {'input': ("aba", "aaaba"), 'result': 2},
    {'input': ("who", "I saw who did that"), 'result': 6},
    {'input': ("where", "I saw who did that"), 'result': -1},
    {'input': ("that", "I saw that you did that"), 'result': 6},
    {'input': ("a", "bcda"), 'result': 3},
    {'input': ("b", "bbbbbb"), 'result': 0}
    ]

levenshtein_edit_distance_tests = [
    {'input': ("a", "aa"), 'result': 1},
    {'input': ("ab", "aa"), 'result': 1},
    {'input': ("zebra in the zoo", "zebra in the zoo"), 'result': 0},
    {'input': ("zebra in the zoo", "cebrain the zoo"), 'result': 2}
]

hamming_distance_tests = [
    {'input': ("1010011", "1001011"), 'result': 2},
    {'input': ("1010011", "1011011"), 'result': 1},
    {'input': ("1010011", "1011010"), 'result': 2},
    {'input': ("abrac", "adabr"), 'result': 4},    
    {'input': ("zebra in the zoo", "zebra in the zoo"), 'result': 0},
    {'input': ("zebra in the zoo", "cebrain  the zoo"), 'result': 4},
    {'input': ("10", "1"), 'result': ValueError}
]

def test_func(func, tests):
    print ("Begin testing " + str(func) + "\n==============================================================")
    for test in tests:
        print ("Test #" + str(tests.index(test)+1) + ":")
        print ("Input: " + str(test["input"]))
        try:
            result = func(*test['input'])
        except Exception as ex:
            result = type(ex)
        finally:
            print ("Expected result: " + str(test["result"]) + "; Produced result: " + str(result) + "\n")
    print("End of tests for " + str(func) + "\n==============================================================")

test_func(kmp, substr_search_tests)
test_func(StringDistance.levenshtein_edit_distance, levenshtein_edit_distance_tests)
test_func(StringDistance.hamming_distance, hamming_distance_tests)
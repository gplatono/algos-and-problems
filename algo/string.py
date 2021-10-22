from typing import *

substr_search_tests = [
    {'input': ("aba", "aaaba"), 'result': 2},
    {'input': ("who", "I saw who did that"), 'result': 6},
    {'input': ("where", "I saw who did that"), 'result': -1},
    {'input': ("that", "I saw that you did that"), 'result': 6},
    {'input': ("a", "bcda"), 'result': 3},
    {'input': ("b", "bbbbbb"), 'result': 0}
    ]

class Trie:
    def __init__(self, prefix):
        self.children = [None] * 26
        self.terminal = False
        #if prefix

    def add(self, prefix):
        first = prefix[0]
        if len(prefix) == 1:
            self.terminal = True
        else:
            if self.children[first] is not None:
                self.children[first].add(prefix[1:])
            else:
                

def prefix_function(s: str) -> List[int]:
    """
    Compute and return the list of prefix function values for the input string s.
    """

    #p - list of prefix function values
    p = [0]*len(s)
    p[0] = 0

    for i in range(1, len(s)):
        #if the current symbol continues the prefix, add it to the previous
        #maximal suffix
        curr = p[i-1]
        while curr >= 0:
            if s[i] == s[curr]:
                p[i] = curr + 1
                break
            elif curr == 0:
                p[i] = 0
                break
            
            curr = p[curr-1]

    return p


def kmp(p: str, s:str) -> int:
    """
    The Knuth-Morris-Pratt substring search algorithm.
    
    Given a string s and a pattern p, return the first index at which p occurs in s.
    
    If p is not a substring of s, return -1
    """

    total = p + s
    prefix = prefix_function(total)
    #print (total, prefix)
    for i in range(len(p), len(total)):
        if prefix[i] == len(p):
            return i-2*len(p) + 1
    
    return -1

def shortest_palindrome_completion(s: str) -> str:
    s1 = s.reverse()
    total = s1 + s


def test_func(func, tests):
    for test in tests:
        result = func(*test['input'])
        print ("Test number " + str(tests.index(test)+1) + ":")
        print ("Input: " + str(test["input"]))
        print ("Expected result: " + str(test["result"]) + "; Produced result: " + str(result) + "\n")        

test_func(kmp, substr_search_tests)

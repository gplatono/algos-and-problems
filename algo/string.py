"""
Custom library of string algorithms. Written for practice and learning.

G. Platonov
11/3/2021
"""

from typing import *

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
                pass

class StringDistance:
    lev_lookup = []

    def levenshtein_edit_distance(a, b):
        """
        Initializes the DP lookup table and computes LED.
        """

        StringDistance.lev_lookup = [[-1] * (len(b)+1) for _ in range(len(a)+1)]
        return StringDistance.led(a, b)
        
    def led(a, b):
        if StringDistance.lev_lookup[len(a)][len(b)] == -1:
            if len(a) == 0 or len(b) == 0:
                StringDistance.lev_lookup[len(a)][len(b)] = max(len(a), len(b))
            elif a[0] == b[0]:
                StringDistance.lev_lookup[len(a)][len(b)] = StringDistance.led(a[1:], b[1:])
            else:
                StringDistance.lev_lookup[len(a)][len(b)] = 1 + min(StringDistance.led(a[1:], b[1:]), 
                                                                    min(StringDistance.led(a, b[1:]), 
                                                                        StringDistance.led(a[1:], b)))
        return StringDistance.lev_lookup[len(a)][len(b)]

    def hamming_distance(a, b):
        """
        Computes Hamming distance between a and b.
        """

        if (len(a) != len(b)):
            raise ValueError("Error: Arguments must have the same length.")
        return sum(a_i != b_i for a_i, b_i in zip(a, b))



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

def manacher(s: str) -> List[int]:
    """
    Compute and return the list of Manacher values for the input string s.
    """
    s = '$#' + '#'.join(s) + '#^'
    n = len(s)
    c = r = 0
    p = [0]*n
    for i in range(1, n-1):
        if i < r:
            p[i] = min(r - i, p[2*c - i])
        while s[i + p[i] + 1] == s[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
    
    return p[1:-1]

print('abacaba', manacher('abacaba'))
print('eracecare', manacher('eracecare'))
print('abba', manacher('abba'))
print('abbarabba', manacher('abbarabba'))
import collections

############################################################
# Problem 3a

def computeMaxWordLength(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    # raise Exception("Not implemented yet")
    return max(sorted(text.split(' '), key=str.lower, reverse=True), key=len)
    # END_YOUR_CODE

############################################################
# Problem 3b

def manhattanDistance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    # raise Exception("Not implemented yet")
    # Manhattan Distance = |x1 - x2| + |y1 - y2|
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    High-level idea: generate sentences similar to a given sentence.
    Given a sentence (sequence of words), return a list of all possible
    alternative sentences of the same length, where each pair of adjacent words
    also occurs in the original sentence.  Notes:
    - The order of the sentences you output doesn't matter.
    - You must not output duplicates.
    - Your generated sentence can use a word in the original sentence more than
      once.
    """
    # BEGIN_YOUR_CODE (around 20 lines of code expected)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as Counters, return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    # raise Exception("Not implemented yet")
    inter = v1 & v2
    result = 0
    for elem in inter:
        result = result + v1[elem]*v2[elem]
    return result
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (around 2 lines of code expected)
    # raise Exception("Not implemented yet")
    for elem in v2:
        v1[elem] = v1[elem] + scale*v2[elem]
    return v1
    # END_YOUR_CODE

############################################################
# Problem 3f

def computeMostFrequentWord(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair: 
        the set of words that occur the maximum number of times, and
	their count, i.e.
	(set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.Counter().
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    # raise Exception("Not implemented yet")
    words = text.split(' ')
    counter = collections.Counter(words)
    countList = counter.most_common()
    maxCount = countList[0][1]
    myList = []
    for elem in countList:
        if elem[1] == maxCount:
            myList.append(elem[0])
        else:
            break
    return (set(myList),maxCount)
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindrome(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (around 20 lines of code expected)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

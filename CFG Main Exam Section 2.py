#CFG Main Exam 

## Section 2

# 2.1.A. 
def count_unique_consonants(s):
    s = s.lower()
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_count = {}
    
    for char in s:
        if char in consonants:
            consonant_count[char] = consonant_count.get(char, 0) + 1
    
    return sum(1 for count in consonant_count.values() if count == 1)

# 2.1.B
# Time Complexity = 0(n) as the function goes through each character in the string once to check if a letter is a constinant 
# an updates the count in the dictionary. These oporations are fairly quick.
# Space complexity = 0(1) The memory needed doesn't grow with the input size as it only stores counts for a maximum of 21 constinants.
# Assumptions: 
# 1. The input contains only english letters. 
# 2. The function can be case-insensitive and converts all letters to lowercase for ease.

# 2.2
def count_squares_recursive(X):
    if X == 0:
        return 0
    return X * X + count_squares_recursive(X - 1)

# X = X by X grid so 3x3 grid is just (3)
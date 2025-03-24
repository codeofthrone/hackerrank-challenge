# Link: https://www.hackerrank.com/challenges/camelcase-4/problem
# Difficulty: Medium
# Solution: Given a string in camelCase, split it into words and vice versa.
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

def CamelCase4():  
    result = []
    for line in sys.stdin:
        obj = line.strip().split(";")
        op, method, words = obj[0], obj[1], obj[2]
        if op == "S":
            # split
            if method == "M":
                # method
                words = words[:-2]
            split_words = []
            temp = ""
            for char in words:
                if char.isupper():
                    if temp:
                        split_words.append(temp)
                    temp = char.lower()
                else:
                    temp += char
            if temp:
                split_words.append(temp)
            result.append(" ".join(split_words))
        elif op == "C":
            # combine
            words = words.split()
            if method == "M":
                # method
                combined = words[0] + "".join(word.capitalize() for word in words[1:]) + "()"
            elif method == "C":
                # class
                combined = "".join(word.capitalize() for word in words)
            elif method == "V":
                # variable
                combined = words[0] + "".join(word.capitalize() for word in words[1:])
            result.append(combined)
            
    for res in result:
        print(res)
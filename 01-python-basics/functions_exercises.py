"""
Python Function Exercises

A collection of beginner Python exercises
completed during my Python learning journey.

Topics:
- Functions
- If / Else Statements
- String Methods
- List Indexing and Slicing
- Loops
"""


# -----------------------------------------
# Exercise 1: Lesser of Two Evens
# -----------------------------------------
# Return the smaller number if both numbers
# are even. Otherwise, return the larger number.


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 4))  # 2
print(lesser_of_two_evens(2, 5))  # 5


# -----------------------------------------
# Exercise 2: Animal Crackers
# -----------------------------------------
# Return True if two words begin with
# the same letter.


def animal_crackers(text):
    if text.split(' ')[0][0] == text.split(' ')[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))  # True
print(animal_crackers('Crazy Kangaroo'))     # False


# -----------------------------------------
# Exercise 3: Old MacDonald
# -----------------------------------------
# Capitalize the first and fourth letters
# of a name.


def old_macdonald(name):
    return name[0].upper() + name[1:3].lower() + name[3].upper() + name[4:].lower()


print(old_macdonald('macdonald'))  # MacDonald


# -----------------------------------------
# Exercise 4: Master Yoda
# -----------------------------------------
# Reverse the order of words in a sentence.


def master_yoda(text):
    return " ".join(text.split(' ')[::-1])


print(master_yoda('I am home'))     # home am I
print(master_yoda('We are ready'))  # ready are We


# -----------------------------------------
# Exercise 5: Has 33
# -----------------------------------------
# Return True if a list contains
# two consecutive 3s.


def has_33(nums):
    i = 0
    for number in nums:
        if i == len(nums) - 1:
            break

        if nums[i] == nums[i+1] == 3:
            return True
        else:
            pass

        i = i + 1

    return False


print(has_33([1, 3, 3]))       # True
print(has_33([1, 3, 1, 3]))    # False
print(has_33([3, 1, 3]))       # False

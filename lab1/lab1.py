#%%
"""
Task 1

Write a function that asks the user for a whole number, and prints
whether the number is even or odd.
"""


#%%
# Test the function
# odd_or_even()


#%%
"""
Task 2

Write a function that calculates and prints the factorial of a number.
The function accepts the number (should be a positive integer) as its 
sole input argument. 
"""


#%%
# Test the function
# print(factorial(5))


#%%
"""
Task 3

Write a function that receives 2 input parameters: 
1) an iterable (items), and 2) a positive integer (n).  
The function returns the lowest n-th value of the iterable. 
If n is not a positive number or it is greater than the number 
of elements in the iterable, the function returns the lowest 
value in the iterable.
"""


#%%
# Test the function with...
# ... a sequence of numbers:
# numbers  = [31, 72, 13, 41, 5, 16, 87, 98, 9]
# print(f"3rd lowest among numbers: {numbers}:")
# print(nth_lowest(numbers,3))

# ... a sequence of letters:
# letters = ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']
# print(f"6th lowest among letters: {letters}:")
# print(nth_lowest(letters, 6))

# ... a string:
# s = "today"
# print(f"2nd lowest in string: '{s}':")
# print(nth_lowest(s, 2))


#%%

"""
Task 4

Write a function that receives a list of numbers and returns
a tuple with the following elements:
- the list element with the smallest absolute value
- the list element with the largest absolute value
- the sum of all non-negative elements in the list
- the product of all negative elements in the list
"""

#%%
# Test the function
# print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, -81]))


#%%
"""
Task 5

Write a function that receives a list of numbers and a threshold value. 
The function:
- creates a new list with unique elements from the input list
  that are below the threshold
- prints the number of elements in the new list
- sorts the elements in the new list in the descending order,
  and prints them, one element per line
"""

#%%
# Test the function
# list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)



#%%
"""
Task 6

Write a function to play a guessing game: to guess a number between 1 and 9.
Scenario: 
- User is prompted to guess a number. 
- If the user guesses wrongly, the prompt reappears
- The user can try to guess max 3 times
- On a successful guess, user should get a "Well guessed!" message, and 
the function terminates. 
- If when guessing, the user enters a number that is out of the bounds 
(less than 1 or greater than 9), or a character that is not a number, 
they should be informed that only single digit values are allowed. This 
does not count as an unsuccessful guessing attempt.

Hints: 
- you can use function 'randint' from 'random' package to generate a number to
be guessed in the game
- the 'isdigit' string function can be used to check if the user's input is a number 
"""



#%%
# Test the function
# guessing_game()


#%%
if __name__ == '__main__':
    pass

    # Task 1
    # odd_or_even()

    # Task 2
    # print(factorial(7))

    # Task 3
    # numbers  = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    # print(f"3rd lowest among numbers: {numbers}:")
    # print(nth_lowest(numbers,3))

    # letters = ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']
    # print(f"6th lowest among letters: {letters}:")
    # print(nth_lowest(letters, 6))

    # s = "today"
    # print(f"2nd lowest in string: '{s}':")
    # print(nth_lowest(s, 2))

    # Task 4
    # print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, -81]))

    # Task 5
    # list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)

    # Task 6
    # guessing_game()

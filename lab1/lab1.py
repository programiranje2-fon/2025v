#%%
# Zadatak 1

def odd_or_even():
    num_str = input("Please enter a whole number\n")
    num = int(num_str)

    # Option 1
    # num_eval = 'EVEN' if num % 2 == 0 else 'ODD'
    # print(f"Number {num} is {num_eval}")

    # Option 2
    _, reminder = divmod(num, 2)
    if reminder == 0:
        print(f"Number {num} is EVEN")
    else:
        print(f"Number {num} is ODD")

#%%
# Test the function
odd_or_even()


#%%
# Zadatak 2

# f = number * (number -1) * ... * 2 * 1
def factorial(number):
    f = 1
    # Option 1
    # for i in range(1, number + 1):
    #     f *= i
    # return f

    # Option 2
    for i in range(number, 0, -1):
        f *= i
    return f


#%%
# Test the function
print(factorial(7))


#%%
# Zadatak 3

def nth_lowest(items, n):
    if n <= 0 or len(items) < n:
        return min(items)
    return sorted(items)[n-1]



#%%
# Test the function with...
# ... a sequence of numbers:
numbers  = [31, 72, 13, 41, 5, 16, 87, 98, 9]
print(f"3rd lowest among numbers: {numbers}:")
print(nth_lowest(numbers,3))

# ... a sequence of letters:
letters = ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']
print(f"6th lowest among letters: {letters}:")
print(nth_lowest(letters, 6))

# ... a string:
s = "today"
print(f"2nd lowest in string: '{s}':")
print(nth_lowest(s, 2))


#%%
# Zadatak 4

def list_stats(numbers):
    min_elem = max_elem = numbers[0]
    sum_non_neg = 0
    prod_neg = 1
    for number in numbers:
        if abs(number) < abs(min_elem):
            min_elem = number
        elif abs(number) > abs(max_elem):
            max_elem = number
        if number >= 0:
            sum_non_neg += number
        else:
            prod_neg *= number
    return min_elem, max_elem, sum_non_neg, prod_neg



#%%
# Test the function
print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, -81]))


#%%
# Zadatak 5
def list_operations(numbers, threshold):
    new_list = []
    for number in numbers:
        if number < threshold and number not in new_list:
            new_list.append(number)
    print(f"Number of elements in the new list: {len(new_list)}")
    new_list.sort(reverse=True)
    for number in new_list:
        print(number)

#%%
# Test the function
list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)



#%%
# Zadatak 6

def guessing_game():
    from random import randint
    number_to_guess = randint(1, 9)
    print("""
        Welcome to the Guessing Game!
        Your task is to guess the number that has been randomly selected among numbers 1 to 9.
        You may try 3 times. Good luck!
    """)
    num_of_attempts = 1
    while True:
        num_str = input("Your guess is: ")
        if not num_str.isdigit() or int(num_str) > 9 or int(num_str) < 1:
            print("Only digits (1-9) are allowed! Please try again, entering a valid value")
            continue
        num = int(num_str)
        if num == number_to_guess:
            print(f"Congrats! You have correctly guessed - the number is {num}")
            return
        if num_of_attempts < 3:
            print(f"Wrong! Please try again - you still have {3 - num_of_attempts} attempts")
            num_of_attempts += 1
        else:
            print("Wrong! Sorry, you've made use of all three attempts. More luck next time")
            return


#%%
# Test the function
guessing_game()


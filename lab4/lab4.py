"""
Vezbe, dvocas 4
"""
from functools import reduce


#%%
# ZADATAK 1

def compute_product(*numbers, squared=False):
    # Option 1
    p = 1
    for num in numbers:
        p *= num**2 if squared else num
    return p
    # Option 2
    # return reduce(lambda a,b: a*b, [num**2 if squared else num for num in numbers])


#%%
# print(compute_product(1,-4,13,2))
# print(compute_product(1, -4, 13, 2, squared=True))
# print()

# Calling the compute_product function with a list
# num_list = [2, 7, -11, 9, 24, -3]
# This is NOT a way to make the call:
# print("Calling the function by passing a list as the argument")
# print(compute_product(num_list))
# print()

# # instead, this is how it should be done (the * operator is 'unpacking' the list):
# print("Calling the function by passing an UNPACKED list as the argument")
# print(compute_product(*num_list))

#%%
# ZADATAK 2
def select_strings(*strings, threshold=3):
    # Option 1
    # selection = []
    # for s in strings:
    #     if s[0].lower() == s[-1].lower() and len(set(s)) > threshold:
    #         selection.append(s)
    # return selection
    # Option 2
    # return [s for s in strings if s[0].lower() == s[-1].lower() and len(set(s)) > threshold]
    # Option 3
    return list(filter(lambda s: s[0].lower() == s[-1].lower() and len(set(s)) > threshold, strings))



#%%
str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']
print(select_strings(*str_list, threshold=4))

#%%
# ZADATAK 3

def process_product_orders(orders, discount=None, shipping=10):
    # Option 1
    # orders_dict = dict()
    # for order_id, _, quantity, item_price in orders:
    #     # order_id, _, quantity, item_price = order
    #     total_price = quantity * item_price
    #     # if discount:
    #     #     total_price *= (1 - discount/100)
    #     total_price *= (1 - discount/100) if discount else 1
    #     # if total_price < 100:
    #     #     total_price += shipping
    #     total_price += shipping if total_price < 100 else 0
    #     orders_dict[order_id] = total_price
    # return orders_dict
    # Option 2
    def compute_total_price(q, ip):
        total_price = q * ip
        total_price *= (1 - discount/100) if discount else 1
        total_price += shipping if total_price < 100 else 0
        return total_price

    # return {order_id: compute_total_price(quantity, item_price) for order_id, _, quantity, item_price in orders}
    # Option 3
    return dict(map(lambda order: (order[0], compute_total_price(order[2], order[3])), orders))

#%%
orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
          ("98762", "Programming Python, Mark Lutz", 5, 56.80),
          ("77226", "Head First Python, Paul Barry", 3, 32.95),
          ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]

print(process_product_orders(orders))
print()
print("The same orders with discount of 10%")
print(process_product_orders(orders, discount=10))

#%%
# ZADATAK 4
import functools
from time import perf_counter
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Nešto uradite pre

        start_time = perf_counter()

        vrednost = func(*args, **kwargs)
        # Nešto uradite posle

        duration = perf_counter() - start_time
        print(f"Execution time of the {func.__name__} function is: {duration}")

        return vrednost

    return wrapper_timer

@timer
def compute_sum_loop(n):
    s = 0
    for x in range(1, n+1):
        # s(x) = 1 + 2 + ... + x
        for i in range(1, x+1):
            s += i
    return s

@timer
def compute_sum_lc(n):
    # 1, 2, ... n
    # S(1), S(2), S(3), ... S(n)
    # sum([S(1), S(2), S(3), ... S(n)])
    # S(x) = 1 + 2 + ... + x
    # S(x) = sum([1, 2, ... x])
    return sum([sum([i for i in range(1, x+1)]) for x in range(1, n+1)])

@timer
def compute_sum_mr(n):
    # 1, 2, ... n -> S(1), S(2), S(3), ... S(n) map
    # S(1), S(2), S(3), ... S(n) -> S(1) + S(2) + S(3) + ... + S(n) reduce
    mapped_values = map(lambda x: sum(range(1,x+1)), range(1, n+1))
    return reduce(lambda a,b: a+b, mapped_values)

#%%
print(compute_sum_loop(10000))
print()
print(compute_sum_lc(10000))
print()
print(compute_sum_mr(10000))

#%%
# ZADATAK 5

def standardiser(func):
    @functools.wraps(func)
    def wrapper_standardiser(*args, **kwargs):
        # Nešto uradite pre
        if all([isinstance(arg, (int, float)) for arg in args]):
            from statistics import mean, stdev
            m = mean(args)
            sd = stdev(args)
            args = [(arg-m)/sd for arg in args]
        else:
            print("Not all positional arguments are numbers; passing them to the function as is")

        print(f"Function {func.__name__} with input parameters:")
        print(", ".join([str(arg) for arg in args]))
        if kwargs:
            print(", ".join([f"{k}={v}" for k, v in kwargs.items()]))

        vrednost = func(*args, **kwargs)
        # Nešto uradite posle
        vrednost = round(vrednost, 4)

        return vrednost

    return wrapper_standardiser

@standardiser
def sum_of_sums(*numbers, n=10):
    # S(x) = 1 + x + x**2 + x**3 + ... + x**n
    mapped_values = map(lambda x:sum([x**i for i in range(0, n+1)]), numbers)
    return reduce(lambda a,b:a+b, mapped_values)


#%%
print(sum_of_sums(1,3,5,7,9,11,13, n=7))
#Prince William M. Tan

# Q1 Type hints

def add(a: int, b: int) -> int:
 return a + b

print("Q1:", add(3, 7))  


# Q2 Lambda function

multiply_by_10 = lambda x: x * 10

print("Q2:", multiply_by_10(5))


# Q3 Defining & calling functions

def greet(name):
    print("Hello " + name + "!")
greet("Alice")


# Q4 map()-Squares of numbers 

nums = [1, 2, 3, 4]

squares =  map(lambda x: x ** 2, nums)

print("Q4:", list(squares))


# Q5 filter() – Keep even numbers

more_nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, more_nums))

print("Q5:", list(evens)) 


# Q6: reduce() – Product of numbers

from functools import reduce
product_nums = [2, 3, 4]

product = reduce(lambda x, y: x * y, product_nums)
print("Q6:", product) 

# Q7: Default arguments

def introduce(name, age=18):

	print(f"My name is {name} and i am {age} years old.")

introduce("Bob", 20) 

# Q8 Closure

def make_add(n):
    def adder(x):
        return x + n
    return adder

add_5 = make_add(10)
print("Q8:", add_5(10)) 

# Q9: Modular-style function

def calculate_average(grades: list[int]) -> float:
    if not grades:
        return 0.0
    
    return sum(grades) / len(grades)
print("Q9:", calculate_average([85, 90, 78])) 

# Q10: Simulated API function

def get_weather(city: str) -> str:
	return f"The Weather in {city} is sunny."
print("Q10:", get_weather("Manila")) 








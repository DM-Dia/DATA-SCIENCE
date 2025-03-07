import time

# Decorator to convert output to uppercase
def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

# Function that returns a greeting message
def say_hello(name):
    return f"Hello, {name}!"

# Applying uppercase_decorator
greet = uppercase_decorator(say_hello)

# Testing the greet function
print(greet("A"))  # Output: "HELLO, A!"

# Timing decorator to measure execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Applying timing_decorator
timed_greet = timing_decorator(greet)

# Testing the timed_greet function
print(timed_greet("A"))

# Logging decorator to log function calls
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Class with methods decorated using logging_decorator
class Math:
    @logging_decorator
    def add(self, a, b):
        return a + b

    @logging_decorator
    def subtract(self, a, b):
        return a - b

# Testing Math class methods
math_obj = Math()
math_obj.add(25, 5)
math_obj.subtract(20, 5)
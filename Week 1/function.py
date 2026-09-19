# Simple example to write a function  
  
# using def keyword to define a function  
def welcome(name): # <--- parameter  
  print(f"Hello, {name}! Welcome to Tpoint Tech!!")  
  
# calling of the defined function  
welcome("John") # <--- argument 

def add(a, b):    
    """This function returns the sum of two numbers."""    
    return a + b    
# Calling the function and storing the result    
result = add(3, 5)    
print(f"The sum is {result}")    

def calculate(a, b):    
    """This function returns the sum and difference of two numbers."""    
    return a + b, a - b    
# Calling the function and unpacking the result    
sum_result, diff_result = calculate(10, 4)    
print(f"Sum: {sum_result}, Difference: {diff_result}")    

def factorial(n):    
    """This function calculates the factorial of a number using recursion."""    
    if n == 1:    
        return 1    
    else:    
        return n * factorial(n - 1)    
# Calling the recursive function    
result = factorial(5)    
print(f"The factorial of 5 is {result}")    

def my_decorator(func):    
    """This is a simple decorator."""    
    def wrapper():    
        print("Something is happening before the function is called.")    
        func()    
        print("Something is happening after the function is called.")    
    return wrapper    
@my_decorator    
def say_hello():    
    print("Hello!")    
# Calling the decorated function    
say_hello()    
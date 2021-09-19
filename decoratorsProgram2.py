#Decorators example

#decorator function to convert to lowercase

def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper
    
    
#decorator function to split the string
def split_decorator(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string
    return wrapper
    
@split_decorator
@lowercase_decorator
def hello():
    return 'Hello World'
    
    
result = hello()
print(result)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def names_decorator(function):
    def wrapper(arg1,arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1,arg2)
        return string_hello
    return wrapper
    
@names_decorator    
def say_hello(name1,name2):
    return 'Hello ' + name1 + '! Hello ' + name2 + '!'
    
print(say_hello('bhupal','anitha'))
    
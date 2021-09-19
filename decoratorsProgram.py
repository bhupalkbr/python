#program for Decorators

# function calling other function
def inc(x):
    return x+1
    
def operator(func, x):
    result = func(x)
    return result
    
print(operator(inc,4))

# function defined inside other function

def print_msg(message):
    greetings = "Hello"
    
    def printer():
        print(greetings, message)
        
    printer()
    
print_msg("Python is awesome")

##########################################

def printer():
    print("Hello World")
    
def display_info(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Execution finished")
      
    return inner
    
    
decorator_func = display_info(printer)
decorator_func()
 
#############################################
#above one can also be written as below

def display_info(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Execution finished")
      
    return inner
    
@display_info
def printer():
    print("Hello World")
    
printer()
###########Decorators with paramters#############

def smart_divide(func):
    
    def inner(a,b):
        print("Dividing", a ,"by" , b)
        if b==0:
            print("cannot deivide by 0!")
            return
        return func(a,b)
    return inner
    
@smart_divide
def divide(a,b):
    return a/b
    
value1 = divide(15,3)
print(value1)
value2 = divide(5,0)
print(value2)

#####################
def star(func):
    def inner(arg):
        print("*"*30)
        func(arg)
        print("*"*30)
        
    return inner

def percent(func):
    def inner(arg):
        print("%"*30)
        func(arg)
        print("%"*30)
        
    return inner

@star    
@percent
def printer(msg):
    print(msg)
    
printer("Decorators are wonderful")

        
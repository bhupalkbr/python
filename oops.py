# OOPS
# Object - which has state & behaviour
# class -  blue print to create object

# class syntax
# class classname:
#   #attributes(properties/state)
#   #functions(methods/behaviour)

#constructor - also a method/function, special method given by python itself
# (__init__(self))
    
class Bottle:
    "the class is used to create a bottle with some parameters"
    #properties/state
    id=1
    logo='abc'
    capacity=1
    height=10
    
    #constructor
    def __init__(self,color,capacity):
        self.color=color
        self.capacity=capacity
        print('constructor')
    #destructor
    def __del__(self):
        print('destructor')
        
    #functions/behaviour
    def wash(self):
        print(self)
        print('washing')
    
    def setCap():
        print('setcap')
    
    def fillWater():
        print('fill water')
        
# object creation
print(Bottle.logo)
bottle1 = Bottle("green",3)
bottle2 = Bottle("yellow",5)
print(bottle1)
print(bottle1.color)
bottle1.wash()

# child class
# class className(ParentClass):
#   #statements

print ("=============child class ================")

class CopperBottle(Bottle):

    def __init__(self,color,capacity):
        #Bottle.__init__(self,color,capacity)
        super().__init__(color,capacity)
        print('child constructor')

    def storeHotWater():
        print('Hot water')
        
print(CopperBottle.logo)

copper1 = CopperBottle("orange",5)
copper1.wash()

print(Bottle.__bases__)
print(CopperBottle.__bases__)
#print(CopperBottle.__class__.bases__)

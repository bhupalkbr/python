#types of inheritance

class class1:
    def join(self):
        print('joined')
        
class class2:
    def subscribe(self):
        print('subscribed')
        
class class3(class1,class2):
    def comment(self):
        print('commented')
        
cl3 = class3()
cl3.subscribe()
cl3.join()
cl3.comment()

# Exception Handling
#common exceptions - ValueError,EOFError,ImportError, IOError, KeyboardInterrupt
# Try , Except
#syntax try:
#           #statements
#       except:
#           #Executes when there is an error
import sys
class Join:
    
    def __init__(self):
        print('constructor')
        
        
    def welcome(self):
        print('welcome')
        
    def __del__(self):
        print('destructor')
        
        
    def members(self):
        try:
            members=['bhupal','anitha','pujya','havish']
            print(members[3])
        except IndexError:
            errorInfo = sys.exc_info()
            print(errorInfo[0],errorInfo[1])
        except IOError:
            print('IO Error')
        except ImportError:
            print('import error')
        except:
            print('Final exception')
        else:
            print('success')
        finally:
            print('I am callled everytime')
        
j1 = Join()
j1.welcome()
j1.members()
 
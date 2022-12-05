
#from sys import path as systemPath
#systemPath.insert(0, './src/')
from delete import deleteDocs

def delete():
    result = print(deleteDocs())
    print(type(result))
    #assert isinstance(result, dict)
    
'''   value = list(result.values())
    for item in value:
        if item == 0:
            print('This file is not delete')
            return False
   
        if item == 1:
            print('this file has been deleted')
            return True'''

if __name__ == "__main__":
    
    delete()
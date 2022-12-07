#To succesfuslly invoke the function 'get_bikes_by_characteristics', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from src.crud_db.find.get_bikes_by_characteristics import get_bikes_by_characteristics
import pytest

@pytest.mark.test_characteristics
def test_is_dict():

    #Assess if the value returned by the function 'get_bikes_by_characteristics' is a dictionary.
    #If it doesn't return a dictionary, it will give an AssertionError and return a message stating it isn't a dictionary.
    assert isinstance(get_bikes_by_characteristics(), dict), "The query doesn't return a dictionary."

if __name__ == '__main__':
    
    test_is_dict()  
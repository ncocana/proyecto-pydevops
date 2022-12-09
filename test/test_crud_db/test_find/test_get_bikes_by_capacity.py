#To succesfuslly invoke the function 'get_bikes_by_capacity', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from src.crud_db.find.get_bikes_by_capacity import get_bikes_by_capacity
import pytest

@pytest.mark.test_capacity
def test_is_dict():

    #Assess if the value returned by the function 'get_bikes_by_capacity' is a dictionary.
    #If it doesn't return a dictionary, it will give an AssertionError and return a message stating it isn't a dictionary.
    assert isinstance(get_bikes_by_capacity(1), dict), "The query doesn't return a dictionary."
    assert isinstance(get_bikes_by_capacity(2), dict), "The query doesn't return a dictionary."
    assert isinstance(get_bikes_by_capacity(3), dict), "The query doesn't return a dictionary."



if __name__ == '__main__':
    
    test_is_dict()  
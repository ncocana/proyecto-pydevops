#To succesfuslly invoke the function 'get_all_data_from_accessories', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from src.queries_db.get_all_data_from_accessories import get_all_data_from_accessories
import pytest

@pytest.mark.test_accessories
def test_is_dict():

    #Assess if the value returned by the function 'get_all_data_from_accessories' is a dictionary.
    #If it doesn't return a dictionary, it will give an AssertionError and return a message stating it isn't a dictionary.
    assert isinstance(get_all_data_from_accessories(), dict), "The query doesn't return a dictionary."

if __name__ == '__main__':
    
    test_is_dict()
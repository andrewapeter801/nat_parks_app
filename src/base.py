import requests
import pandas as pd

class Base:
    '''
    Class that handles all connections to the API object and returns a DataFrame from it's initialization.

    Class that has the following methods:
    return_url: returns the api_url we are currently working with
    get_data: scrapes the dat from the API and creates a DataFrame
    '''
    def __init__(self, url = 'requests.get(f"{base_url}{endpoint}", params=params)'):
        self.api_url = url
        self.get_data()

    def get_data(self):
        '''Scrapes the data from the API and creates a DAtaFrame from it'''
        self.df = pd.DataFrame.from_dict(pass) # need to add requests.get
        return self.df
    
if __name__=='__main__':
    c = Base()
    print(c.df)
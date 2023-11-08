from base import Base
import pymongo
import os
from dotenv import load_dotenv

# Class Declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from our Base class to MongoDB instance.
    Initializes an instance of the inherited class.

    Definded methods are as follows:
    upload_one_by_one: Upload pieces of information to a database one by one over an iterable structure.
    upload_collection: Uploads an entire collection of documents to MongoDB.
    delete_collection: Drops an entire collection of data from the database.
    '''

    def __init__(self, user='bionicman', password='xsDirYQKVYrbkPjW'):
        # initialize an instance of our inherited class:

        # Load in the env variables:
        load_dotenv()
        self.user=user
        self.password=password
        self.__mongo_url=os.getenv('MONGO_URL')


        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.__mongo_url)

        #Create the database
        self.db = self.client.db

        # create/connect to a collection
      # Create a collection:
        self.park_info = self.db.park_info
        # Set dataframe index to the id column:
        
        
    def upload_collection(self):
        self.park_info.insert_many([self.df.to_dict()])

    def upload_one_by_one(self):
        self.park_info.drop()
        Base.__init__(self)     #<---add the dunders to init
        self.df.set_index('id', inplace=True)
        for i in self.df.index:
            self.park_info.insert_one(self.df.loc[i].to_dict())
        
if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all Park Info to Mongo')
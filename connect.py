import pymongo
from pymongo import MongoClient
import urlquote
import urllib.parse
from pymongo import errors
import razorpay
from hmac import HMAC
from cryptography.fernet import Fernet

import modelConfig

class studieconnect(object):
    __instance = None


def __init__(self):
    #self.connect = self.funconnect()
    """make constructor private"""
    if studieconnect.__instance is not None:
        raise Exception("this class is singleton, use studieconnect.get_instance() instead.")
    else:
        studieconnect.__instance = self
        self.__mongoclient = None
        #self.__storeconfig = None

def __initsourceconfig(self):
    #self.__storeconfig = ConfigManager.getconfig(Names.CONFIG_STORE)
    if self.__mongoclient is None:
        USERNAME = urllib.parse.quote_plus(modelConfig.DATABASE_UID)
        PASSWORD = urllib.parse.quote_plus(modelConfig.DATABASE_PWD)
        HOST = modelConfig.DATABASE_HOST
        PORT = str(modelConfig.DATABASE_PORT)
        DATABASE = modelConfig.DATABASE_NAME

        CONNECTION_STRING = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.jpyuamu.mongodb.net/?retryWrites=true&w=majority"
        #CONNECTION_STRING = 'mongodb://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(PORT) + '/' + DATABASE

        self.__mongoclient = MongoClient(CONNECTION_STRING)

def __getdb(self):
    self.__initsourceconfig()
    DATABASE = modelConfig.DATABASE_NAME
   
    return self.__mongoclient.get_database(self.__storeconfig[DATABASE])


@staticmethod
def get_instance():
    if studieconnect.__instance is None:
        studieconnect.__instance = studieconnect()

    return studieconnect.__instance

def findAll(self, collName, findQuery):
    db = self.__getdb()
    metricDataList = []
    queryResultList = db.get_collection(collName).find(findQuery)
    for queryResult in queryResultList:
        metricDataList.append(queryResult)
    return metricDataList

def storeOneDoc(self, collName, storingDoc):
    db = self.__getdb()
    db.get_collection(collName).insert_one(storingDoc)

def updateOneDoc(self, collName, findQuery, updateQuery):
    db = self.__getdb()
    db.get_collection(collName).update_one(findQuery, updateQuery)

def findOneDoc(self, collName, findQuery):
    db = self.__getdb()
    metricDataList = []
    queryResultList = db.get_collection(collName).find(findQuery).limit(1)
    for queryResult in queryResultList:
        metricDataList.append(queryResult)
    return metricDataList[0]


#return=s JSON data for one document
def findOne(self, collName, findQuery):
    db = self.__getdb()
    queryResult = db.get_collection(collName).find(findQuery).limit(1)
    return queryResult




def funconnect(self):
    try:
        USERNAME = urllib.parse.quote_plus(modelConfig.DATABASE_UID)
        PASSWORD = urllib.parse.quote_plus(modelConfig.DATABASE_PWD)
        HOST = modelConfig.DATABASE_HOST
        PORT = str(modelConfig.DATABASE_PORT)
        DATABASE = modelConfig.DATABASE_NAME

        CONNECTION_STRING = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.jpyuamu.mongodb.net/?retryWrites=true&w=majority"

        #CONNECTION_STRING =  'mongodb://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+str(PORT)+'/'+DATABASE

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)

    except ConnectionError as CE:
        print(CE)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client[modelConfig.DATABASE_NAME]




def mongoconnect():
        print('fdfd')



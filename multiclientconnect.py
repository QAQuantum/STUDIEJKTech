import pymongo
from pymongo import MongoClient
import urlquote
import urllib.parse
from pymongo import errors
from hmac import HMAC
from cryptography.fernet import Fernet
from typing import Any
import modelConfig
import datetime
apiDateTime = datetime.datetime.now()
import pandas as pd
from bson.int64 import Int64

connectionDict = {}

class multiclientconnecting(object):
    __instance = None


    def __init__(self):
        #self.connect = self.funconnect()
        """make constructor private"""
        if multiclientconnecting.__instance is not None:
            raise Exception("this class is singleton, use studieconnect.get_instance() instead.")
        else:
            multiclientconnecting.__instance = self
            self.__mongoclient = None
            self.questionGenerator = None

            #self.__storeconfig = None


    def __initsourceconfig(self,jsondata):
        #self.__storeconfig = ConfigManager.getconfig(Names.CONFIG_STORE)
        if(len(connectionDict) > 0):
            if(jsondata['DBNAME'] in connectionDict):
                #print("KEY present")
                self.__mongoclient = connectionDict[jsondata['DBNAME']]
                # print(self.__mongoclient)
                # print(" ============================    CLIENT FROM LOOP 1 ")
            else:
                # print("KEY ABSENT")
                # print(" CONSTRUCTING THE CUSTOMER DB KEY   ", jsondata['DBNAME'])
                self.DBNAME = jsondata['DBNAME']
                self.DBUID = jsondata['DBUID']
                self.DBPWD = jsondata['DBPWD']
                self.DBHOST = jsondata['DBHOST']
                self.DBPORT = jsondata['DBPORT']
                USERNAME = urllib.parse.quote_plus(self.DBUID)
                PASSWORD = urllib.parse.quote_plus(self.DBPWD)
                HOST = jsondata['DBHOST']
                PORT = jsondata['DBPORT']
                DATABASE = jsondata['DBNAME']
                CONNECTION_STRING = 'mongodb://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(
                    PORT) + '/' + DATABASE
                self.__mongoclient = MongoClient(CONNECTION_STRING)  # unicode_decode_error_handler='ignore'
                connectionDict[jsondata['DBNAME']] = self.__mongoclient
                # print(self.__mongoclient)
                # print(" ----------------------------    CLIENT FROM LOOP 2 ")
            # for keys,val in connectionDict.items():
        else:
            # print("connection  has NO  values ADDDING CONNECTIONS FIRST TIME  ")
            # print(" CONSTRUCTING THE CUSTOMER DB KEY   ", jsondata['DBNAME'])
            self.DBNAME = jsondata['DBNAME']
            self.DBUID = jsondata['DBUID']
            self.DBPWD = jsondata['DBPWD']
            self.DBHOST = jsondata['DBHOST']
            self.DBPORT = jsondata['DBPORT']
            USERNAME = urllib.parse.quote_plus(self.DBUID)
            PASSWORD = urllib.parse.quote_plus(self.DBPWD)
            HOST = jsondata['DBHOST']
            PORT = jsondata['DBPORT']
            DATABASE = jsondata['DBNAME']
            CONNECTION_STRING = 'mongodb://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(
                PORT) + '/' + DATABASE
            self.__mongoclient = MongoClient(CONNECTION_STRING)  # unicode_decode_error_handler='ignore'
            connectionDict[jsondata['DBNAME']] = self.__mongoclient
            # print(self.__mongoclient)
            # print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    CLIENT FROM LOOP 0 ")





    def __getdb(self,jsondata):
        self.__initsourceconfig(jsondata)
        #DATABASE = self.DBNAME
        DATABASE =   jsondata['DBNAME']
        # print("DATABSE  " , jsondata)
        # print(DATABASE)
        return self.__mongoclient.get_database(DATABASE)

    def get_instance(multiclientconnecting):
        if multiclientconnecting.__instance is None:
            multiclientconnecting.__instance = multiclientconnecting()

        return multiclientconnecting.__instance



    def deleteOneDoc(self, collName, findQuery,jsondata):
        db = self.__getdb(jsondata)
        db.get_collection(collName).delete_one(findQuery)


    def deleteManyDoc(self, collName, findQuery,jsondata):
        db = self.__getdb(jsondata)
        db.get_collection(collName).delete_many(findQuery)


    def updateOneDoc(self, collName, findQuery, updateQuery,jsondata):
        db = self.__getdb(jsondata)
        db.get_collection(collName).update_one(findQuery, updateQuery)


    def findOneDoc(self, collName, findQuery,jsondata):
        db = self.__getdb(jsondata)
        metricDataList = []
        queryResultList = db.get_collection(collName).find(findQuery).limit(1)
        for queryResult in queryResultList:
            metricDataList.append(queryResult)
        return metricDataList[0]


    def findDocwithLimit(self, collName, findQuery,jsondata, limitCount):
        db = self.__getdb(jsondata)
        metricDataList = []
        queryResultList = db.get_collection(collName).find(findQuery).limit(limitCount)
        for queryResult in queryResultList:
            metricDataList.append(queryResult)
        return metricDataList


    #return=s JSON data for one document
    def findOne(self,collName, findQuery,jsondata):
        db = self.__getdb(jsondata)
        #print("DB DETAILS  " , db)

        queryResult = db.get_collection(collName).find_one(findQuery)
        #print("QUERY FROM MCC   after confirmation --------------------------------------------       " , queryResult)
        return queryResult

    def findAll(self,collName, findQuery,jsondata):
        db = self.__getdb(jsondata)
        queryResultList = db.get_collection(collName).find(findQuery).sort('_id', pymongo.DESCENDING)
        # for queryResult in queryResultList:
        #     metricDataList.append(queryResult)
        return queryResultList


    def findandCount(self,collName, findQuery,jsondata):
        db = self.__getdb(jsondata)
        queryResultList = db.get_collection(collName).find(findQuery)
            #db.get_collection(collName).find(findQuery).sort('_id', pymongo.DESCENDING)
        # for queryResult in queryResultList:
        #     metricDataList.append(queryResult)
        #print(queryResultList)
        return queryResultList


    def countAllDocuments(self, collName, findQuery,jsondata):
        db =  self.__getdb(jsondata)
        recordCount  = db.get_collection(collName).count_documents(findQuery)
        return  recordCount




    def aggregateDocuments(self, collName, findQuery, jsondata):
        db =  self.__getdb(jsondata)
        details = db.get_collection(collName).aggregate(findQuery)
        print(type(details))
        payload = []
        for data in details:
            payload.append(data)
        return payload

    def findAllwithSkipLimit(self,collName, findQuery,start,end,jsondata):
        db = self.__getdb(jsondata)
        metricDataList = []
        queryResultList = db.get_collection(collName).find(findQuery).sort('_id', -1).skip(start).limit(end)
        # for queryResult in queryResultList:
        #     metricDataList.append(queryResult)
        return queryResultList

    def updateOne(self,collName, findQuery,updateQuery,jsondata):
        db = self.__getdb(jsondata)
        queryResult = db.get_collection(collName).update_one(findQuery,updateQuery)
        return queryResult


    def updateMany(self,collName, findQuery,updateQuery,jsondata):
        db = self.__getdb(jsondata)
        queryResult = db.get_collection(collName).update_many(findQuery,updateQuery)
        return queryResult


    def updatearrayOne(self,collName, findQuery,updateQuery, filterArray,jsondata):
        db = self.__getdb(jsondata)
        queryResult = db.get_collection(collName).update_one(findQuery,updateQuery, array_filters=filterArray)
        return queryResult

    def updateOnewithUpsert(self,collName, findQuery,updateQuery, status,jsondata):
        db = self.__getdb(jsondata)
        queryResult = db.get_collection(collName).update_one(findQuery,updateQuery,upsert=status)
        return queryResult

    def storeOneDoc(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        try:
            data = db.get_collection(collName).insert_one(storingDoc)
        except pymongo.errors.WriteError:
            print("Exception at STOREONEDOC")
        return data




    def storeOneDoc_USEREXAMINATION(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_USEREXAMINATION Error 2")

        return data



    def storeOneDoc_FILES_USER(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_FILES_USER Error 2")

        return data



    def storeOneDoc_OCR_USER(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_OCR_USER Error 2")

        return data


    def storeOneDoc_FILES_PROFESSOR(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_FILES_PROFESSOR Error 2")

        return data




    def storeOneDoc_VIDEOFILES_USER(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_VIDEOFILES_USER Error 2")

        return data


    def storeOneDoc_UNIVERSITYSETTINGS(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_UNIVERSITYSETTINGS Error 2")

        return data



    def storeOneDoc_USER_ExamStarter(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_USEREXAMINATION Error 2")

        return data


    def storeOneDoc_USER_ExamCreator(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_USEREXAMINATION Error 2")

        return data

    def storeOneDoc_UNIQUE(self, collName, storingDoc,jsondata):
        db = self.__getdb(jsondata)
        data = ''
        listStore = []
        listStore.append(storingDoc)
        for docs in listStore:
            try:
                data = db.get_collection(collName).insert_one(docs)
            except pymongo.errors.DuplicateKeyError:
                while pymongo.errors.DuplicateKeyError:
                    docs['_id'] += 1
                    try:
                        data = db.get_collection(collName).insert_one(docs)
                        break
                    except pymongo.errors.DuplicateKeyError:
                        print("Came with storeOneDoc_UNIQUE Error 2")

        return data


    def mongoconnect(self):
        try:
            print("NOT NEEDED ANYMORE")
          

        except ConnectionError as CE:
            print(CE)
        ########### Create the database for our example (we will use the same database throughout the tutorial
        #return client[modelConfig.DATABASE_NAME]



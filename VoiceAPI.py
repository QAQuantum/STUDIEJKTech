import json
from flask import Flask, jsonify, render_template , request, redirect,  url_for, copy_current_request_context
import os
from flask_cors import CORS, cross_origin
from urllib.parse import unquote
from PIL import Image
import io
import fitz
import uuid
import requests
import datetime
import pandas as pd
import calendar
import random
import time
import httpx
import sys, asyncio
from threading import Thread, ThreadError
from datetime import timedelta
from datetime import date
import razorpay
from cryptography.fernet import Fernet
import random
from random import randint
import re
from itertools import chain
import pymongo
from pymongo import errors
import os
import json
import urllib.parse
import urllib.request
from bson.int64 import Int64
from connect import mongoconnect
from deep_translator import GoogleTranslator
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, BertTokenizer
import numpy as np
from AI_LLM.StabilityAI import stabilityAImodel
from AI_LLM.BardAI import bardAImodel
import modelConfig
from ModelSettings.modeldetails import modeldetails
from ModelSettings.videoextractor import videoApps
from SuggestDetails.suggestion import suggestdetails
from SuggestDetails.videoTextTranslator import textTranslator
from EmailSettings.sendMail import sendMail
from CourseSettings.coursedetails import coursedetails
from PaymentDetails.paydetails import paydetails
from orgSettings.organization import orgApps
from workShop.worksopApps import workshopApps
from universitySettings.university import univsityApps
from superadminSettings.superadmin import superadminApps
from MCQSettings.mcqstudie import mcqstudieApps
from CalendarSettings.CalendarApps import CalendarApps
from LibrarySettings.libraryApps import libraryApps
#from universitySettings.universityhaystackdocument import haystackdocumentApps
from LLMSettings.LLMInterview import LLMInterviewApps
from AccessSettings.AccessForm import AccessApps
from LMSSettings.LMSDetails import lmsdetails
from fileProcessingDetails.fileExtractor import fileExtraction
from OCRSettings.ocrAnalysis import ocrApps
from OCRSettings.haystackocr import haystackocrApps
from VideoSettings.videoData import videoApps
from defaultSettings.defaultuniversitysettings import defaultApps
from templateSettings.studietemplates import templateApps
from recommendationSettings.recommendationApp import recommendDetails
from guidanceSettings.guidanceApp import guidanceDetails
from JKSummarization.DataManagerApps import DataManagerApps
from AI_LLM.OPENAIModel import openAImodel
from pymemcache.client import base
from fastapi import BackgroundTasks, FastAPI
import dropbox
from dropbox import exceptions as DropBoxExceptions
import http.client
import requests

#HAYSTACK DETAILS BELOW
from haystack.nodes import QuestionGenerator
from haystack.nodes import TransformersSummarizer
from haystack import Document
from haystack.nodes import EntityExtractor


model_Technology = "deepset/roberta-base-squad2"
filelocation_Technology = './models/modelComputerScience/encoded.json'
from connect import  studieconnect, mongoconnect
from studieconnect import studieconnecting
from multiclientconnect import multiclientconnecting

import feedparser

app = Flask(__name__)
#run_with_ngrok(app)
CORS(app)


if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


grok_api  = ""
import os

# ------OPENAI DETAILS
import openai
import openai as bookai
import openai as scaleai
import openai as interviewai
import openai as interviewanswersai
model_Name ="text-davinci-003"



# ----ENCRYPTION KEY DETAILS
key2 = Fernet.generate_key()
cannotChange_Key = "*********="
key =  str(cannotChange_Key).encode()
fline = Fernet(key)



# we are charging 10% for all the topics sold
percentageRatio =  0.1
studieThreadName = modelConfig.THREAD_NAME

@cross_origin(origin='*')
@app.route('/', methods=['GET'])
def indexs():
  email = request.args.get('email')
  return jsonify({'email': email})



@cross_origin(origin='*')
@app.post("/summarizeHandler")
def jkSummarizationDetails():
    getJobDetails = json.loads(request.data)
    getJobDetails = json.loads(getJobDetails)
    apiDateTime = datetime.datetime.now()
    dateSeparator = pd.date_range(str(apiDateTime), periods=1, freq='D')
    sessionID = (getJobDetails['sessionid'])
    userid = (getJobDetails['user'])
    apiKey = (getJobDetails['guidKey'])
    promptID = (getJobDetails['promptID'])
    promptProvided = (getJobDetails['promptProvided'])
    sentenceToSummarise = (getJobDetails['sentenceToSummarise'])
    summariseLength = Int64(getJobDetails['summariseLength'])
    summariseInLanguage = (getJobDetails['summariseInLanguage'])

    keyAssessments = {
        "APICallTime": str(apiDateTime),
        "userid": userid,
        "sessionID": sessionID,
        "apiKey":apiKey,
        "_id": calendar.timegm(time.gmtime()) * 1000,
        "promptID":promptID,
        "promptProvided":promptProvided,
        "sentenceToSummarise":sentenceToSummarise,
        "summariseLength":summariseLength,
        "summariseInLanguage":summariseInLanguage
    }
    

    #JSON sent to JK Data Manager
    try:
        jsonData = {}
        unvDetails.jsondata = keyAssessments
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        jsonData = loop.run_until_complete(jkOject.summarizationDataManager())
        return jsonify(jsonData)
    except Exception as e:
        print("Exception in Search", str(e))
        jsonData['Status'] = 'Fail'
        return jsonify(jsonData)
    finally:
        loop.close()




if __name__ == "__main__":

   
    jkOject = DataManagerApps()
    MCC = multiclientconnecting.get_instance(multiclientconnecting)  # ALL SECONDARY DB CONNECTIONS
    SC = studieconnecting.get_instance(studieconnecting)
   
    context = ('/etc/letsencrypt/live/api.studie.academy/cert.pem', '/etc/letsencrypt/live/api.studie.academy/privkey.pem')
    app.run(host='0.0.0.0', port=5000, threaded=True, ssl_context=context)

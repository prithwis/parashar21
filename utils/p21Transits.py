#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
import p21
import p21utils
import p21utilsR
import p21swe
#import p21YogInfo
# ------------------------------------------------
# required for multiple imports of the same module
# ------------------------------------------------
import importlib
importlib.reload(p21)
importlib.reload(p21utils)
importlib.reload(p21utilsR)
importlib.reload(p21swe)
#importlib.reload(p21YogInfo)

#Utility functions
#from pymongo import MongoClient
import pandas as pd
import dateutil
import json
#from docx import Document
#from docx.shared import Inches
#from docx.enum.text import WD_ALIGN_PARAGRAPH
#rom datetime import datetime
from datetime import timedelta
import pytz

from datetime import datetime, timedelta
import pytz
#from google.colab import files

#import matplotlib.pyplot as plt
#import math

import os
from IPython.display import HTML
from base64 import b64encode

# ------------------------------------------------
# transit functions
# ------------------------------------------------

def getDelta(cD,bA,aA,bR,aR,AllTransits = False):
    #print('getDelta',cD)
    cDs = cD.strftime("%d %b %y")+'|'
    grahaList = p21.Graha + ['Ra','Ke']
    #for G in p21.Graha:
    for G in grahaList:
        if bA[G] != aA[G]:
            #if G not in ['Mo', 'Me']:               # Excludes certain grahas to reduce the clutter
            if G not in ['Mo']:               # Excludes certain grahas to reduce the clutter
                print(cDs, G, 'TRANSITS from ', bA[G], 'to ', aA[G])
            else:
                if AllTransits:
                    print(cDs, G, 'transits from ', bA[G], 'to ', aA[G])
            #print(cDs, G, 'transits from ', bA[G], 'to ', aA[G])
        if bR['GRet'][G] != aR['GRet'][G]:
            #print(cD,G, 'changes from ', bR['GRet'][G], 'to ', aR['GRet'][G], ' retrograde')
            if bR['GRet'][G]:
                print(cDs, G, 'turns DIRECT')
            else:
                print(cDs, G, 'turns RETRO')
		
# ------------------------------------------------
		
def Transitz(numberOfDays,allTransits = False,buildMovie = False):
    sDate = datetime.now(pytz.timezone('Asia/Kolkata'))

    # Replace this with any custom date string
    custom_date_str = "2025-12-01 00:00:01"  # format: YYYY-MM-DD HH:MM:SS
    # Convert string to datetime object and localize to Asia/Kolkata timezone
    #sDate = pytz.timezone('Asia/Kolkata').localize(datetime.strptime(custom_date_str, "%Y-%m-%d %H:%M:%S"))

    cDate = sDate

    p21utils.setTransitData(p21utils.getTransitData(cDate))

    # -----------------------------------------
    # initial graha positions
    print("Transit Information")
    print("START DATE:", cDate.strftime("%d %b %Y %H:%M"))
    print("INITIAL GRAHA POSITIONS:")

    grahaList = p21.Graha + ['Ra', 'Ke']
    positions = []

    for G in grahaList:
        rashi = p21.GRashiA[G]
        retro = p21.GLonRet['GRet'][G]

        position = f"{G}: {rashi}"
        if retro:
            position += " (RETRO)"

        positions.append(position)

    print(" | ".join(positions))
    print("-" * 40)
    # -----------------------------------------

    for count in range(numberOfDays):

        prevGrashiA = p21.GRashiA
        prevGLonRet = p21.GLonRet
        cDate += timedelta(days=1)

        p21utils.setTransitData(p21utils.getTransitData(cDate))
        if buildMovie:
            p21.cID = cDate.strftime("%d %b %y")
            #p21utilsR.R12B_drawChart_South()
            p21utilsR.R12B_drawChart_Bengal()
            newName = './cImages/img'+str(count)+'.png'
            oldName = './RashiChart.png'
            os.rename(oldName, newName)
        getDelta(cDate,prevGrashiA,p21.GRashiA,prevGLonRet,p21.GLonRet,allTransits)
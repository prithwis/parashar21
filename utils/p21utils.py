#Utility functions 

import pandas as pd
import dateutil
import matplotlib.pyplot as plt
import math
#import string_utils
import p21
# ---------------------------------------------
#converting dict{ionary} to list and back

d2l = lambda dic: [(k, v) for (k, v) in dic.items()]
l2d = lambda lis: dict(lis)

#converts a Rashi number to the Rashi name
#
RashiName = ["RashiName","Ari","Tau","Gem","Can","Leo","Vir","Lib","Sco","Sag","Cap","Acq","Pis"]
def RashiN2A(n):
    return RashiName[n]

# ----------------------------------------------
def generateChartTxt():
    global txt
    txt = ['']*13
    for g,r in p21.GRashiN.items():
        if r == 1:
            txt[1]= txt[1]+' '+g+('/R' if GRet[g] else '')
        if r == 2:
            txt[2]= txt[2]+' '+g+('/R' if GRet[g] else '')
        if r == 3:
            txt[3]= txt[3]+' '+g+('/R' if GRet[g] else '')
        if r == 4:
            txt[4]= txt[4]+' '+g+('/R' if GRet[g] else '')
        if r == 5:
            txt[5]= txt[5]+' '+g+('/R' if GRet[g] else '')
        if r == 6:
            txt[6]= txt[6]+' '+g+('/R' if GRet[g] else '')
        if r == 7:
            txt[7]= txt[7]+' '+g+('/R' if GRet[g] else '')
        if r == 8:
            txt[8]= txt[8]+' '+g+('/R' if GRet[g] else '')
        if r == 9:
            txt[9]= txt[9]+' '+g+('/R' if GRet[g] else '')
        if r == 10:
            txt[10]= txt[10]+' '+g+('/R' if GRet[g] else '')
        if r == 11:
            txt[11]= txt[11]+' '+g+('/R' if GRet[g] else '')
        if r == 12:
            txt[12]= txt[12]+' '+g+('/R' if GRet[g] else '')
            
    for i in range(1,13):
        if len(txt[i]) == 0:
            txt[i] = '*'
#print(txt[1],txt[2],txt[3],txt[4],txt[5],txt[6],txt[7],txt[8],txt[9],txt[10],txt[11],txt[12],)

# Plots the chart in the Bengal Format


def drawChart_Bengal():

    ChartFile = p21.pName+p21.ChartType+'.png'
    generateChartTxt()

    #id = ChartType+'\n'+pName+'\n'+pDate+'\n'+pTime+'\n'+pPlace
    id = p21.ChartType+'\n'+pName
    if p21.ChartType == 'Rashi':
        ChartColour = 'orange'
    else:
        ChartColour = 'olive'
    
        
    #plt.figure(figsize=(7,7))
    plt.figure(figsize=(7,7),facecolor=ChartColour)
    
    plt.axis('off')

    # draw vertical line 
    plt.plot([30, 30], [0, 90], 'k-', lw=2)
    plt.plot([60, 60], [0, 90], 'k-', lw=2)

    # draw horizontal line 
    plt.plot([0, 90], [30, 30], 'k-', lw=2)
    plt.plot([0, 90], [60, 60], 'k-', lw=2)

    #draw diagonal lines
    plt.plot([60,90],[60,90], 'k-', lw=2)
    plt.plot([0,30],[90,60], 'k-', lw=2)
    plt.plot([0,30],[90,60], 'k-', lw=2)
    plt.plot([0,30],[0,30], 'k-', lw=2)
    plt.plot([60,90],[30,0], 'k-', lw=2)

    plt.text(32, 38, id, fontsize=12)

    plt.text(32, 82, txt[1], fontsize=12)
    plt.text(8, 82, txt[2], fontsize=12)
    plt.text(2, 62, txt[3], fontsize=12)
    plt.text(2, 45, txt[4], fontsize=12)
    plt.text(2, 25, txt[5], fontsize=12)
    plt.text(8, 5, txt[6], fontsize=12)
    plt.text(32, 5, txt[7], fontsize=12)
    plt.text(62, 5, txt[8], fontsize=12)
    plt.text(68, 25, txt[9], fontsize=12)
    plt.text(68, 45, txt[10], fontsize=12)
    plt.text(68, 62, txt[11], fontsize=12)
    plt.text(62, 82, txt[12], fontsize=12)

    
    #plt.savefig("CurrentChart.png", bbox_inches='tight')
    plt.savefig(ChartFile, bbox_inches='tight')
    plt.show()

    
print ("drawChart_Bengal defined")
# ----------------------------------------------------------

# Convert the longitude of a Graha into its Rashi of residence
#
# Navamsa is different
# http://www.oocities.org/talk2astrologer/LearnAstrology/Details/Navamsa.html
#
# the logic for placing a Graha in a 'Navamsa' Rashi is as follows
# starting from Longitude 0 [ 'Normal' Aries / Mesha start point]
# upto Longitude 360, we divide the longitudes in 108 partitions with each 
# partition being 3.33333 degrees. These 108 partitions are now numbered 
# sequentially, except that once we reach 12, the next partition is 1, not
# 13. So we have 9 sequences running from 1 - 12 each. The number corresponding
# to the partition where the Graha falls is the Navamsa Rashi of the Graha


def Long2Rashi(x):
    print('L2R',p21.ChartType)
    if p21.ChartType == 'Rashi':
        RashiNumber = math.floor(x[1]/30)+1
        return x[0],RashiNumber
    if p21.ChartType == 'Navamsa':
        N1 = math.floor(x[1]/3.333333)+1
        N2 = N1%12
        if N2 == 0:
            RashiNumber = 12
        else:
            RashiNumber = N2
        return x[0],RashiNumber

def LocateGrahaInRashi():
    
    #Defines the Horoscope in terms of locating planets in their Rashis
    #
    print('Loc',p21.ChartType)
    p21.GRashiN = l2d(list(map(lambda x : Long2Rashi(x), d2l(p21.GLon))))
    print(p21.GRashiN)

    p21.GRashiA = {}
    for k,v in GRashiN.items():
        GRashiA[k] = RashiN2A(v)
        
    print(p21.GRashiA)
    
# ------------------------------------------------
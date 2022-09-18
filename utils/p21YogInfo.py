#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
# Yog Texts, Conditions

#global yogText, yogCond
yogText={}
yogCond = {}
# 1 Gajakesari Yog
#yogText['Gajakesari'] = 'Gajakesari^ yog : Moon and Jupiter is placed in the 1st, 4th, 7th and 10th house which forms the angular houses or Kendra. ^ ref : https://www.astroyogi.com/kundli/yog'
youText['Gajkesari'] = 'Gajakesari Yog^ Jupiter is in Kendra or 1,4,7,10th from Moon^ ref BVRaman Page 13'
yogCond['Gajakesari'] = {"$or":[
                                 "$and": [
                                    'GRashiN.Mo' : {'$eq': 1}}
                                    {"$or" : [
                                      {'GRashiN.Ju' : {'$eq': 4}},
                                      {'GRashiN.Ju' : {'$eq': 7}},
                                      {'GRashiN.Ju' : {'$eq': 10}}
                                    ]
                                 ]
                                 "$and": [
                                    'GRashiN.Mo' : {'$eq': 2}}
                                    {"$or" : [
                                      {'GRashiN.Ju' : {'$eq': 5}},
                                      {'GRashiN.Ju' : {'$eq': 8}},
                                      {'GRashiN.Ju' : {'$eq': 11}}
                                    ]
                                 ]
                                ]
                        }






                            
#
# BudhAdiya Yog
#BudhAdityaText = 'Budhaditya^ yog formed by the conjunction of Sun and Mercury.  Considered to be a very auspicious Yoga. ^ ref : https://www.astroyogi.com/kundli/yog'            
#BudhAdityaCond = {'GConjunctsG2.Su' : {'$in': ['Me']}}       # Su conjunct Me   

yogText['BudhAditya'] = 'Budhaditya^ yog formed by the conjunction of Sun and Mercury.  Considered to be a very auspicious Yoga. ^ ref : https://www.astroyogi.com/kundli/yog'    
yogCond['BudhAditya'] = {'GConjunctsG2.Su' : {'$in': ['Me']}}       # Su conjunct Me   
#
#BudhAditya Yog without Mercury Retrograde
yogText['BudhAdityaNR'] = 'Budhaditya_NR^ yog formed by the conjunction of Sun and Mercury where Mercury NOT retrograde. ^ ref : https://www.astroyogi.com/kundli/yog'            
yogCond['BudhAdityaNR'] = {"$and":
                        [
                         {'GConjunctsG2.Su' : {'$in': ['Me']}},       # Su conjunct Me   
                         {'GRet.Me' : {'$eq': False}}                # Me NOT retrograde  
                        ]
                   } 
#

#RajaYog
yogText['Rajyog'] = 'Raj^  yog : Jupiter is in Cancer, Venus in the ninth house and Jupiter in the seventh house.^ ref : https://www.astroyogi.com/kundli/yog'
yogCond['Rajyog'] = {"$and":
                    [
                        {'GRashiN.Ju': {'$eq': 4}},               # Jupiter in Cancer
                        {'GrahaBhava.Ju' : {'$eq': 7}} ,            # Jupiter in 7th House
                        {'GrahaBhava.Ve' : {'$eq': 9}}             # Jupiter in 7th House

                    ]
              }
#
#Chandra Mangal (Mahalakshmi) Yog
yogText['ChandraMangal1'] = 'ChandraMangal1^ yog : Moon Conjunct Mars, both Exalted, and NOT in 3rd, 6th, 8th, 12th house. ^ ref : https://www.astroyogi.com/kundli/yog/mahalaxmi'
yogCond['ChandraMangal1'] = {"$and":
                    [
                        {'exaltG.Ma': {'$eq': True}},               # Exalted Mars
                        {'exaltG.Mo': {'$eq': True}},               # Exalted Mo
                        {'GConjunctsG2.Ma' : {'$in': ['Mo']}} ,     # Ma conjunct Mo     
                        {'GrahaBhava.Mo' : {'$nin': [3,6,8,12]}} ,    # Mo not in 3,6,8,12
                    ]
         }
         
yogText['ChandraMangal2'] = 'ChandraMangal2^ yog : Moon Conjunct Mars, neither debilitated, and NOT in 3rd, 6th, 8th, 12th house. ^ ref : https://www.astroyogi.com/kundli/yog/mahalaxmi'
yogCond['ChandraMangal2'] = {"$and":
                    [
                        {'debilG.Ma': {'$eq': False}},               # not debilitated Mars
                        {'debilG.Mo': {'$eq': False}},               # not debilitated Moon
                        {'GConjunctsG2.Ma' : {'$in': ['Mo']}} ,     # Ma conjunct Mo        
                        {'GrahaBhava.Mo' : {'$nin': [3,6,8,12]}} ,    # Mo not in 3,6,8,12
                        
                    ]
         }
#
#Dhan Yog
#
yogText['DhanYog0'] = 'DhanYog0^  : Conjunctions of Lords of Different Houses ^ ref : LHAE KN Rao, pg 77'
yogCond['DhanYog0'] = {"$or":
                    [
                        { 'BLConjunctsBL2.1': {'$in': ['2','5','9','11']} }, # 1st Lord Conjuncts 2,5,9,11 Lord
                        { 'BLConjunctsBL2.2': {'$in': ['5','9','11']} }  ,
                        { 'BLConjunctsBL2.5': {'$in': ['9','11']} } ,
                        { 'BLConjunctsBL2.9': {'$in': ['11']} }  
                    ]
         }

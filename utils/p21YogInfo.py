# 𝓟𝓪𝓻𝓪𝓼𝓱𝓪𝓻21
# 𝓟𝓻𝓲𝓽𝓱𝔀𝓲𝓼 𝓜𝓾𝓴𝓮𝓻𝓳𝓮𝓮
# --------------------------------------------------
# Yog Texts, Conditions

global yogText, yogCond, yogDummy
yogText={}
yogCond = {}
yogDummy = 'Dummy'
# BudhAdiya Yog
#BudhAdityaText = 'Budhaditya^ yog formed by the conjunction of Sun and Mercury.  Considered to be a very auspicious Yoga. ^ ref : https://www.astroyogi.com/kundli/yog'            
#BudhAdityaCond = {'GConjunctsG2.Su' : {'$in': ['Me']}}       # Su conjunct Me   

yogText['BudhAditya'] = 'Budhaditya^ yog formed by the conjunction of Sun and Mercury.  Considered to be a very auspicious Yoga. ^ ref : https://www.astroyogi.com/kundli/yog'    
yogCond['BudhAditya'] = {'GConjunctsG2.Su' : {'$in': ['Me']}}       # Su conjunct Me   
#
#BudhAditya Yog without Mercury Retrograde
BudhAdityaNRText = 'Budhaditya_NR^ yog formed by the conjunction of Sun and Mercury where Mercury NOT retrograde. ^ ref : https://www.astroyogi.com/kundli/yog'            
BudhAdityaNRCond = {"$and":
                        [
                         {'GConjunctsG2.Su' : {'$in': ['Me']}},       # Su conjunct Me   
                         {'GRet.Me' : {'$eq': False}}                # Me NOT retrograde  
                        ]
                   } 
#
#Gajakesari Yog
GajakesariText = 'Gajakesari^ yog : the moon and Jupiter is placed in the 1st, 4th, 7th and 10th house which forms the angular houses or Kendra. ^ ref : https://www.astroyogi.com/kundli/yog'
GajakesariCond = {"$and":
                    [
                        {'GConjunctsG2.Ju' : {'$in': ['Mo']}},      # Ju conjunct Mo 
                        { "$or" : [
                            {'GrahaBhava.Mo' : {'$eq': 1}},              # Mo in First House
                            {'GrahaBhava.Mo' : {'$eq': 4}},              # Mo in Fourth House
                            {'GrahaBhava.Mo' : {'$eq': 7}},              # Mo in Seventh House
                            {'GrahaBhava.Mo' : {'$eq': 10}}              # Mo in Tenth House
                          ]
                        }  

                    ]
                 }           
#
#RajaYog
RajYogText = 'Raj^  yog : Jupiter is in Cancer, Venus in the ninth house and Jupiter in the seventh house.^ ref : https://www.astroyogi.com/kundli/yog'
RajYogCond = {"$and":
                    [
                        {'GRashiN.Ju': {'$eq': 4}},               # Jupiter in Cancer
                        {'GrahaBhava.Ju' : {'$eq': 7}} ,            # Jupiter in 7th House
                        {'GrahaBhava.Ve' : {'$eq': 9}}             # Jupiter in 7th House

                    ]
              }

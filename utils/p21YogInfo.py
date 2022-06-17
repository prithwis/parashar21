# 𝓟𝓪𝓻𝓪𝓼𝓱𝓪𝓻21
# 𝓟𝓻𝓲𝓽𝓱𝔀𝓲𝓼 𝓜𝓾𝓴𝓮𝓻𝓳𝓮𝓮
# --------------------------------------------------
# Yog Texts, Conditions
# BudhAdiya Yog
BudhAdityaText = 'Budhaditya^ yog formed by the conjunction of Sun and Mercury.  Considered to be a very auspicious Yoga. ^ ref : https://www.astroyogi.com/kundli/yog'            
BudhAdityaCond = {'GConjunctsG2.Su' : {'$in': ['Me']}}       # Su conjunct Me   
#
#BudhAditya Yog without Mercury Retrograde
BudhAdityaNRText = 'Budhaditya_NR^ yog formed by the conjunction of Sun and Mercury where Mercury NOT retrograde. ^ ref : https://www.astroyogi.com/kundli/yog'            
BudhAdityaNRCond = {"$and":
                        [
                         {'GConjunctsG2.Su' : {'$in': ['Me']}},       # Su conjunct Me   
                         {'GRet.Me' : {'$eq': False}}                # Me NOT retrograde  
                        ]
                   } 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

from Utils import *

#global wars for paths to the .txt files
#based on http://www.itim.org.il/%D7%9E%D7%90%D7%92%D7%A8-%D7%A9%D7%9E%D7%95%D7%AA/
NAME_HE_DICT = "dictionaries/namesHE.txt"
#based on https://github.com/dominictarr/random-name
NAME_ENG_DICT = "dictionaries/namesENG.txt"
SURNAME_HE_DICT = "dictionaries/surnamesHE.txt"
SURNAME_ENG_DICT = "dictionaries/surnamesENG.txt"
CITY_HE_DICT = "dictionaries/citiesHE.txt"
CITY_ENG_DICT = "dictionaries/citiesENG.txt"
COUNTRY_HE_DICT = "dictionaries/countriesHE.txt"
COUNTRY_ENG_DICT = "dictionaries/countriesENG.txt"
#based on https://github.com/danielgulloa/jobMatch
SKILL_HARD_HE_DICT = "dictionaries/skillsHARDhe.txt"
SKILL_HARD_ENG_DICT = "dictionaries/skillsHARDeng.txt"
SKILL_SOFT_HE_DICT = "dictionaries/skillsSOFThe.txt"
SKILL_SOFT_ENG_DICT = "dictionaries/skillsSOFTeng.txt"
LANGUAGES_HE_DICT = "dictionaries/languagesHE.txt"
LANGUAGES_ENG_DICT = "dictionaries/languagesENG.txt"
        
class Dictionary(object):

        #basic dictionaries for lookup
        name_he         = set()
        name_eng        = set()
        surname_he      = set()
        surname_eng     = set()
        city_he         = set()
        city_eng        = set()
        country_he      = set()
        country_eng     = set()
        skill_hard_he   = set()
        skill_hard_eng  = set()
        skill_soft_he   = set()
        skill_soft_eng  = set()
        language_he     = set()
        language_eng    = set()
        

        """
        c'tor
        fills the dictionaries from files
        """
        def __init__(self):
                self.name_he            = loadFromFile(NAME_HE_DICT)
                self.name_eng           = loadFromFile(NAME_ENG_DICT)
                self.surname_he         = loadFromFile(SURNAME_HE_DICT)
                self.surname_eng        = loadFromFile(SURNAME_ENG_DICT)
                self.city_he            = loadFromFile(CITY_HE_DICT)
                self.city_eng           = loadFromFile(CITY_ENG_DICT)
                self.country_he         = loadFromFile(COUNTRY_HE_DICT)
                self.country_eng        = loadFromFile(COUNTRY_ENG_DICT)
                self.skill_hard_he      = loadFromFile(SKILL_HARD_HE_DICT, '\n')
                self.skill_hard_eng     = loadFromFile(SKILL_HARD_ENG_DICT, '\n')
                self.skill_soft_he      = loadFromFile(SKILL_SOFT_HE_DICT, '\n')
                self.skill_soft_eng     = loadFromFile(SKILL_SOFT_ENG_DICT, '\n')
                self.languages_he       = loadFromFile(LANGUAGES_HE_DICT, '\n')
                self.languages_eng      = loadFromFile(LANGUAGES_ENG_DICT, '\n')
                print "Finished loading dictionaries.\n"


        """
        add new word into dictionary
        """
        def addWord(self, dict_name, word):
                if(word not in getattr(self, dict_name)):
                        #add word into dictionary object
                        getattr(self, dict_name).add(word)
                        print "Adding new word '" + word + "' into dictionary..."
                        #update dictionary file
                        path = globals()[dict_name.upper() + "_DICT"]
                        addToFile(path, word)
                        
                
                

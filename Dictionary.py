#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

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
LANGUAGES = "dictionaries/languages.txt"
        
class Dictionary(object):

        #fields
        namesHE = set()
        namesENG = set()
        surnamesHE = set()
        surnamesENG = set()
        citiesHE = set()
        citiesENG = set()
        countriesHE = set()
        countriesENG = set()
        skillsHARDhe = set()
        skillsHARDeng = set()
        skillsSOFThe = set()
        skillsSOFTeng = set()
        languages = set()
        
        """
        load data from file into set
        """
        @staticmethod
        def loadFromFile(path):
                print "Loading data from " + path + "..."
                f = io.open(path, 'r', encoding='utf-8').read()
                #create new set with data from file
                return set(f.split())
        """
        load data from file into set line by line
        """
        @staticmethod
        def loadFromFileByLine(path):
                print "Loading data from " + path + "..."
                f = io.open(path, 'r', encoding='utf-8').read()
                #create new set with data from file
                return set(f.split('\n'))

        """
        c'tor
        fills the dictionaries from files
        """
        def __init__(self):
                self.namesHE = Dictionary.loadFromFile(NAME_HE_DICT)
                self.namesENG = Dictionary.loadFromFile(NAME_ENG_DICT)
                self.surnamesHE = Dictionary.loadFromFile(SURNAME_HE_DICT)
                self.surnamesENG = Dictionary.loadFromFile(SURNAME_ENG_DICT)
                self.citiesHE = Dictionary.loadFromFile(CITY_HE_DICT)
                self.citiesENG = Dictionary.loadFromFile(CITY_ENG_DICT)
                self.countriesHE = Dictionary.loadFromFile(COUNTRY_HE_DICT)
                self.countriesENG = Dictionary.loadFromFile(COUNTRY_ENG_DICT)
                self.skillsHARDhe = Dictionary.loadFromFileByLine(SKILL_HARD_HE_DICT)
                self.skillsHARDeng = Dictionary.loadFromFileByLine(SKILL_HARD_ENG_DICT)
                self.skillsSOFThe = Dictionary.loadFromFileByLine(SKILL_SOFT_HE_DICT)
                self.skillsSOFTeng = Dictionary.loadFromFileByLine(SKILL_SOFT_ENG_DICT)
                self.languages = Dictionary.loadFromFileByLine(LANGUAGES)
                print "Finished loading dictionaries\n"

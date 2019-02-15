#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import regex
#import os

class Resume:
    'class for parsed resume data'

    #resume converted into plain text
    plain_text = ""

    #word list after splitting resume into words
    word_list = []

    #string object for first and last name
    name = None
    #israeli ID
    id = None
    #year of birth
    birthday = None
    #list of provided phones
    phone = []
    #list of provided e-mails
    e_mail = []
    #list of educational organizations
    edu = []
    #list of workplaces
    exp = []
    #set of hard skills
    skill_h = set()
    #set of soft skills
    skill_s = set()
    #set of language knoweledges
    lang = set()
    
    '''
    c'tor
    init values for data acquired from simple resume scan
    '''
    def __init__(self, text, words):
        self.plain_text = text #unicode(text, 'utf8')
        self.word_list = words[:] #slicing for deep copy
        

    '''
    string of list objects
    '''
    def listToString(self, lst):
        s = ""
        if(len(lst) == 1):
            s = lst[0]
        else:
            s = ", ".join(lst)
        if(len(s) > 2 and s[0] == ','):
            return s[2:]
        else:
            return s


    '''
    print set data
    '''
    def setToString(self, st):
        s = ""
        if(len(st) == 1):
            s = st.pop()
        else:
            s = ", ".join(st)
        if(len(s) > 2 and s[0] == ','):
            return s[2:]
        else:
            return s
        

    '''
    string of object data
    '''
    def toString(self):
	#default response
        d = "Not Found"      
                
        s = "Resume data:\n============\nName:\n\t"
        s = (s + d) if (self.name == None) else (s + self.name)

        s += "\n\nID:\n\t"
        s = (s + d) if (self.id == None) else (s + self.id)

        s += "\n\nBirthday:\n\t"
        s = (s + d) if (self.birthday == None) else (s + self.birthday)
        
        s += "\n\nPhone:\n\t"
        s = (s + d) if (self.phone == []) else (s + self.listToString(self.phone))
        
        s += "\n\nE-mail:\n\t"
        s = (s + d) if (self.e_mail == []) else (s + self.listToString(self.e_mail))

        s += "\n\nEducation:\n\t"
        s = (s + d) if (self.edu == []) else (s + self.listToString(self.edu))

        s += "\n\nExperience:\n\t"
        s = (s + d) if (self.exp == []) else (s + self.listToString(self.exp))

        s += "\n\nSkills:\n\t"
        s = (s + d) if (len(self.skill_h) == 0) else (s + self.setToString(self.skill_h))

        s += "\n\nQualities:\n\t"
        s = (s + d) if (len(self.skill_s) == 0) else (s + self.setToString(self.skill_s))
        
        s += "\n\nLanguages:\n\t"
        s = (s + d) if (len(self.lang) == 0) else (s + self.setToString(self.lang))

        #resulted string
        return s + '\n'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import punctuation
import re

from Dictionary import Dictionary
from FileReader import FileReader
from Resume import Resume

#global vars for file reading
PATH = "files/"
EXTENSION = ".doc"

#global vars for different types of spaces
SPACE = 32
NO_BREAK_SPACE = 160

class Parser:
    
    #dictionary data for lookups
    dictionary = None
    #list of resumes for parsing
    resume_list = []
    
    """
    c'tor
    init Dictionary object
    """
    def __init__(self):
        print "New Instanse of Parser is Created\n"
        #load dictionary data
        self.dictionary = Dictionary()

        
    """
    create list of words from text string
    """
    @staticmethod
    def splitTextIntoList(text):
        #list of words created from provided text
        words = []
        words = text.replace(':',' ').replace(';',' ').replace(',',' ').replace('\t',' ').replace('\/',' ').replace('\\',' ').replace('(',' ').replace(')',' ').split()
        for idx in range(0, len(words)):
            words[idx] = ''.join(words[idx].split())
            words[idx] = words[idx].strip(punctuation)
        return words   
        
    
    '''
    check resume for useful data based on assumed format
    '''
    def formatMatchHeName(self, index):
        #print self.resume_list[index].plain_text
        word = "שם:"
        word = unicode(word, 'utf8')
        #debug
        #print word
        w_len = len(word)
        #debug
        #print self.plain_text
        #self.plain_text = unicode(self.plain_text, 'utf8')
        idx = self.resume_list[index].plain_text.find(word)
        if(idx == -1):
            #search for match w/o ':'
            w_len -= 1
            idx = self.resume_list[index].plain_text.find(word[:len(word) - 1])
            #debug
            #print word[:len(word) - 1]        
        else:
            #debug
            #print "======!!!!!======"
            #print "Found word " + word + " via Word Lookup"
 
            #take text till first tab or till new line as name
            end = self.resume_list[index].plain_text.find('\t', idx + w_len)
            if(end == -1):
                end = self.resume_list[index].plain_text.find('\n', idx + w_len)
            line = self.resume_list[index].plain_text[idx + len(word):end]
            
            #strip whitespace from both ends
            line = line.strip()
            #remove leading semicolon
            if(line[0] == ':'):
                line = line[1:]
                #strip whitespace from both ends
                line = line.strip()
           
            #take words separated by single space only
            end = len(line)
            for i in range(1, len(line)):
                #debug
                #print ord(line[i])
                if( (ord(line[i]) == SPACE and (ord(line[i - 1]) == NO_BREAK_SPACE)) or (ord(line[i]) == NO_BREAK_SPACE and (ord(line[i - 1]) == SPACE)) or (ord(line[i]) == SPACE and (ord(line[i - 1]) == SPACE)) or (ord(line[i]) == NO_BREAK_SPACE and (ord(line[i - 1]) == NO_BREAK_SPACE)) or (line[i] == '\t')) :
                    end = i - 1
                    break

            #print end
            #print line[:end]
            #print len(line[:end])
            
            self.resume_list[index].name = line[:end]
            return True
        return False

        
    """
    dictionary lookup for HEBREW name
    """
    def dictMatchHeName(self, index):
        resume = self.resume_list[index]
        name = None
        for idx in range(0, len(resume.word_list)):
            #debug
            #print "checking " + resume.word_list[idx] + " in the dict of names"
            if resume.word_list[idx] in self.dictionary.namesHE:
                #debug
                #print "word " + resume.word_list[idx] + " is found in the dict"
                #check if its not part of the CV heading
                if(idx > 0):
                    #debug
                    #print "Prev word is: " + resume.word_list[idx - 1]
                    word = "קורות"
                    word = unicode(word, 'utf8')
                    if(resume.word_list[idx - 1] != word):
                        if(resume.word_list[idx + 1][0:4].isnumeric() == False):
                            name = resume.word_list[idx] + " " + resume.word_list[idx + 1]
                            break
                else:
                    if(resume.word_list[idx + 1][0:4].isnumeric() == False):
                        name = resume.word_list[idx] + " " + resume.word_list[idx + 1]
                        break
        resume.name = name
        if(name != None):
            return True
        else:
            return False


    """
    dictionary lookup for ENGLISH name
    """
    def dictMatchEngName(self, index):
        resume = self.resume_list[index]
        name = None
        for idx in range(0, len(resume.word_list)):
            #debug
            #print "Checking " + resume.word_list[idx] + " in the dict of names"
            if resume.word_list[idx] in self.dictionary.namesENG:
                #debug
                #print "Word " + word_list[idx] + " is found in the dict"
                if(resume.word_list[idx + 1][0:4].isnumeric() == False):
                    name = resume.word_list[idx] + " " + resume.word_list[idx + 1]
                    break
        resume.name = name


    """
    check if provided number is legal ID
    """
    def checkID(self, id):
        sum = 0      
        for i in range(0, 9):
            n = int(id[i])
            #debug
            #print "num=" + str(n)
            n = n * ((i % 2) + 1)
            if(n < 10):
                sum += n
            else:
                sum += (n - 9)
        if(sum % 10 == 0):
            return id
        else:
            return None
        
    '''
    """
    detect phone by compare
    """
    def isPhone(self, index):
        resume = self.resume_list[index]
        text = resume.plain_text
        
        found_phone = None
        match = re.search('(?:\+ *)?\d[\d\- ]{7,}\d', text)
        if(match != None):
            found_phone = match.group(0)
            if(len(found_phone) == 9):
                if(found_phone.isnumeric()):
                    if(checkID(found_phone) != True):
                        #if number is 9 digit length and fails ID check
                        
                        return True
                    else:
                        return False
            
            num = re.sub('[^0-9]','', found_phone)
            #for israeli numbers
            if(len(num) >= 9 and len(num) <= 15):
                return True         
        else:
            return False
    '''

        
    """
    detect phone using pattern matching
    """
    def findPhonePattern(self, index):
        resume = self.resume_list[index]
        text = resume.plain_text

        phone_list = []
        phones = re.findall('(?:\+ *)?\d[\d\- ]{7,}\d', text)
        for phone in phones:
            ph_lst = phone.split()
            for p in ph_lst:
                #check if consists of numbers after removing dashes
                number = re.sub('[^0-9]','', p)
                if(len(number) >= 9 and len(number) <= 15):
                    if(number.isnumeric()):
                        if(len(p) == 9):
                            if(self.checkID(p) == None):
                                #if number is 9 digit length and fails ID check
                                phone_list.append(p)
                            else:
                                resume.id = p
                        else:
                            phone_list.append(p)

        resume.phone = phone_list[:]
        
        
    """
    find e-mail address in text string
    """
    def findEmail(self, index):
        resume = self.resume_list[index]
        text = resume.plain_text
        
        e_mails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        resume.e_mail = e_mails


    """
    create list of hard skills
    """
    def findHardSkills(self, index):
        resume = self.resume_list[index]
        text = resume.plain_text
        dictionary = self.dictionary.skillsHARDeng

        for skill in dictionary:
            s1 = " " + skill.lower() + " "
            s2 = " " + skill.lower() + ","
            if((text.lower().find(s1) != -1) or (text.lower().find(s2) != -1)):
                if(len(skill) == 1):
                    skill = skill[0].upper()
                elif(len(skill) >= 1):
                    skill = skill[0].upper() + skill[1:]
                self.resume_list[index].skill_h.add(skill)
    
    
    """
    create list of soft skills
    """
    def findSoftSkills(self, index):
        resume = self.resume_list[index]
        text = resume.plain_text
        dictionary = self.dictionary.skillsSOFTeng
        
        for skill in dictionary:
            s1 = " " + skill.lower() + " "
            s2 = " " + skill.lower() + ","
            if((text.lower().find(s1) != -1) or (text.lower().find(s2) != -1)):
                if(len(skill) == 1):
                    skill = skill[0].upper()
                elif(len(skill) >= 1):
                    skill = skill[0].upper() + skill[1:]
                resume.skill_s.add(skill)

    """
    create list of languages
    """
    def findLanguages(self, index):
        resume = self.resume_list[index]
        text = resume.plain_text
        dictionary = self.dictionary.languages
        
        for language in dictionary:
            s1 = " " + language.lower() + " "
            s2 = " " + language.lower() + ","
            if((text.lower().find(s1) != -1) or (text.lower().find(s2) != -1)):
                resume.lang.add(language) 


    """
    parse resume at given index from resume list
    """
    def parse(self):
        print "Parsing in progress...\n"
        file_reader = FileReader(PATH, EXTENSION)
        file_reader.getFileList()
 
        #get text from all .doc files
        file_reader.readAllFiles()

        
        #create Resume object for each text file
        for text in file_reader.text_list:    

            #debug
            #print text
            #text = file_reader.docToText(f)
            word_list = self.splitTextIntoList(text)
            resume = Resume(text, word_list)
            #add resume to parser's list of resumes
            self.resume_list.append(resume)


        #for each resume object in the parser's list
        for idx in range(0, len(self.resume_list)):
            #debug
            #print "Resume Object Before Parsing:"
            #print parser.resume_list[idx].toString()

            #GET NAME
            #if format matching didn't work - try dictionary lookup
            if(self.formatMatchHeName(idx) == False):
                if(self.dictMatchHeName(idx) == False):
                    #try to match using english dictionary
                    self.dictMatchEngName(idx)

            #GET BIRTHDAY:TODO

            #GET PHONE
            #get phone by pattern match - if failed, check by comparing each 
            if(self.findPhonePattern(idx) == False):
                self.findPhoneCompare(idx)

            #GET E-MAIL
            self.findEmail(idx)

            #GET HARD SKILLS
            self.findHardSkills(idx)

            #GET SOFT SKILLS
            self.findSoftSkills(idx)

            #GET LANGUAGES
            self.findLanguages(idx)



            #print parser.resume_list[idx].skill_h
            print "\n*****************************************************************************************************************"
            #debug
            print "Full path to resume file: " + file_reader.file_list[idx] + "\n"
            #print "Resume Data After Parsing:"
            print  "\n" + self.resume_list[idx].toString()
        print "#################################################Parsing finished!!!###################################################\n"

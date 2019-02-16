#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from string import punctuation


"""
load data from text file into set based on delimiter
if no provided - split by whitespace
"""
def loadFromFile(path, delimiter=None):
    words = set()
    print "Loading data from " + path + "..."
    f = io.open(path, 'r', encoding='utf-8')
    text = f.read()
    #create new set with data from file
    if(delimiter == None):
        words = set(text.split())
    else:
        words = set(text.split(delimiter))
    f.close()
    return words
    


"""
write text data to file at the given path
"""
def addToFile(path, data):
    #append data at new line
    f = io.open(path, 'a', encoding='utf-8')
    f.write('\n' + data)
    f.close()
    
    
"""
save string data as a text file
"""
def writeToFile(file_name, data):
    #write data to file
    print "Saving file " + file_name + ".txt file..."
    f = io.open(file_name, 'w', encoding='utf-8')
    f.write(data.encode('utf-8'))
    f.close()


"""
create list of words from text string
punctuation is stripped from each word
"""
def splitTextIntoList(text):
    #list of words created from provided text
    words = []
    words = text.replace(':',' ').replace(';',' ').replace(',',' ').replace('\t',' ').replace('\/',' ').replace('\\',' ').replace('(',' ').replace(')',' ').split()
    for idx in range(0, len(words)):
        words[idx] = words[idx].strip(punctuation)
    return words   

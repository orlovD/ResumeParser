#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile

#global vars for parsing .doc files
#based on https://gist.github.com/mikeckennedy/c79fcbcbb96be9c13cc16fbc707ea5ee
"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

class FileReader:
    
    #path to files
    path = ""
    #extension to look for
    ext = ""
    #list of files with full paths
    file_list = []
    #list with text from read files
    text_list = []


    """
    c'tor
    set path to files and extension
    """
    def __init__(self, path, extension):
        self.path = path
        self.ext = extension


    """
    receive path to directory with files to read
    create list of files with given extension
    """
    def getFileList(self):
        #list for files with full paths
        paths = []
        for folder, dirs, files in os.walk(self.path):
            for f in files:
                if f.endswith(self.ext):
                    full_path = os.path.join(folder, f)
                    #debug
                    #print full_path
                    #add each full path of .doc file to list
                    self.file_list.append(full_path)


    #based on https://gist.github.com/mikeckennedy/c79fcbcbb96be9c13cc16fbc707ea5ee
    """
    read all files from directory with files to read
    create list of text data from each file
    """
    def readAllFiles(self):
        for path in self.file_list:
            """
            Take the path of a docx file as argument, return the text in unicode.
            """
            print "Reading file " + path + "..."
            document = zipfile.ZipFile(path)
            xml_content = document.read('word/document.xml')
            document.close()
            tree = XML(xml_content)

            paragraphs = []
            for paragraph in tree.getiterator(PARA):
                texts = [node.text
                         for node in paragraph.getiterator(TEXT)
                         if node.text]
                if texts:
                    paragraphs.append(''.join(texts))

            #create string
            data = '\n\n'.join(paragraphs)
            self.text_list.append(data)

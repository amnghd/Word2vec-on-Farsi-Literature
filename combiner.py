# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:07:43 2019

@author: Amin
"""

import glob

read_files = glob.glob("poems/*.txt") # reading all the files into one list

with open("poems/whole_farsi_corpus.txt", "w", encoding="utf8") as outfile:
    for f in read_files:
        with open(f, "r", encoding="utf8") as infile:
            outfile.write(infile.read())
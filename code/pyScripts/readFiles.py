# This is a testing python script
# Simply used to read in text from various n2c2 data sets and perform

###############
# XML Files
###############


#xmlPath = "/home/laura/Documents/Spring2023/NLP/data/Tempor/trainingJuly2012/"

from bs4 import BeautifulSoup
#with open('8.xml', 'r') as f:
#    data = f.read()


#print(data)



#######################
###### MEDI DATA ######
#######################


# Specify a path. Doesn't actually need to be too specific. Can concat strings to be more detailed.
training_path = "/home/laura/Documents/Spring2023/NLP/data/Medi/training.sets.released/1/106886"



f = open(training_path)
#yourList = f.readlines()
yourList = [line.rstrip('\n') for line in f]
#for lines in yourList:
    #print(lines)


# A way to iterate over basic txt files, that don't have the .txt
# There is a command line fix for this but not currently working. May be due to git? Unsure
import glob
paths = glob.glob("/home/laura/Documents/Spring2023/NLP/data/Medi/training.sets.released/1/*")
print(paths[0])


# or
# A lot of ways to handle files

import os
#arr = os.listdir()
#arr = os.listdir('c:\\files')

##
# Basic text processing from ABD.
# May be useful to keep handy when handling small sets of N2C2 data locally.
#
##

# Imports required
import os
import re
#nltk.download('stopwords')
from nltk.corpus import stopwords

# File path
pathtxt = "/home/laura/Documents/Spring2023/NLP/data/Tempor/trainJulytxt/"

# Empty lists to contain data and ratings
corpus = []
train_targets = []

# Stop words might actually be necessary when look at time relationships
stop_words = set(stopwords.words('english'))

# Cut this down
def wordProccessing(document):
    newDoc = []
    for sents in document:
        sents = sents.lower()
        sents = sents.split()
        for words in sents:
            if words not in stop_words:
                newDoc.append(words)
    return newDoc


for file in os.listdir(pathtxt):

    filePath = pathtxt + file
    with open(filePath, encoding="utf8") as f:
        currentDoc = f.readlines()
        currentDoc = wordProccessing(currentDoc)
        corpus.append(str(currentDoc))

print(corpus[1])

#####
# Saving results to CSV
# corpus.to_csv("Data_Read", sep=',', index=False, encoding='utf-8')

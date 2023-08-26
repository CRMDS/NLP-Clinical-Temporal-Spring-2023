# Basic xml reading in python.
# Can be used on xml files that contain both the original
# clinical notes, as well as the event, timex3 and tlink tags associated.

from bs4 import BeautifulSoup
import glob

# Collect all paths of all .xml files
paths = glob.glob("/home/laura/Documents/Spring2023/NLP_Data/Tempor/trainingJuly2012/*.xml")

# Lists to hold the text/tags. Not sure if this is the best object
textClin = []
tagsClin = []

def main():
    for i in range(0, (len(paths))):
        with open(paths[i], 'r') as f:
            data = f.read()
            # Extract out the original clinical notes
            bs_data = BeautifulSoup(data, "xml")
            clin_text = bs_data.find('TEXT')
            textClin.append(clin_text)

            # Extract out the tags associated with the clinical notes
            clin_tags = bs_data.find('TAGS')
            tagsClin.append(clin_tags)

    # print out random text to check
    print(textClin[8])

if __name__ == '__main__':
    main()



from flair.data import Sentence
from flair.nn import Classifier

# 1. make example sentence
sentence = Sentence("George was born in Washington")
#print(sentence)

# 2. Load entity tagger and predict entities
tagger = Classifier.load('ner')
tagger.predict(sentence)

# check which named entities have been found in the sentence
#entities = sentence.get_labels('ner')
#for entity in entities:
    #    print(entity)

# 3. load relation extractor
extractor = Classifier.load('relations')

# predict relations
extractor.predict(sentence)


# check which relations have been found
relations = sentence.get_labels('relation')
for relation in relations:
    print(relation)

for label in sentence.get_labels('relation'):
    print(label)

from flair.nn import Classifier
from flair.data import Sentence

# load the model
tagger = Classifier.load('ner')

# make a sentence
sentence = Sentence('George Washington went to Washington')

# predict NER tags
tagger.predict(sentence)

# print the sentence with tags

#print(sentence)

## Accessing the individual predictions

#for label in sentence.get_labels():
#    print(label)


## values for each prediction
# For each prediction, you can directly access the label value, it's score
# and the entity text

for label in sentence.get_labels():
    print(f'label.value is: "{label.value}"')
    print(f'label.score is: "{label.score}"')
    print(f'the text of label.data_point is: "{label.data_point.text}"\n')

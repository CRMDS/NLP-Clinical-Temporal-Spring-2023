from flair.data import Sentence

#sentence = Sentence("The grass is green.")

#print(sentence)
# Outputs the sentence

# Iterating over tokens in a sentence
#for token in sentence:
    #    print(token)


# Directing accessing a toke

# using the token id
#print(sentence.get_token(4))

# using the index itself
#print(sentence[3])


# Tokenization

# add a NER tag to tokwn 3 in the sentence
#sentence[3].add_label('ner', 'color')

# Only the word green has a label associated with this NER tag
#print(sentence)

# Labelling a whole sentence
# Example with sentiment label
#sentence = Sentence('The grass is green.')
#sentence.add_label('sentiment', 'POSITIVE')
#print(sentence)

# You can also do multiple labels
# and also access the labels

sentence = Sentence('The grass is green.')
sentence[3].add_label('ner', 'color')
sentence.add_label('sentiment', 'POSITIVE')

for label in sentence.get_labels():
    print(label)


# If we only wanted ner

# get_labels('ner'):


# Information for each label

sen_2 = Sentence('The sky is blue.')
sen_2[3].add_label('ner','color')

for label in sen_2.get_labels():
    print(f'"{label.data_point.text}" is classified as "{label.value}" with score {label.score}')

from flair.nn import Classifier
from flair.data import Sentence

# similar to last file (predictions)
sentence = Sentence('George Washington went to Washington')
tagger = Classifier.load('ner-fast')
tagger.predict(sentence)
print(sentence)

# Tagging with the best, large transformer based model
# Use it if accuracy is more important than speed/memor

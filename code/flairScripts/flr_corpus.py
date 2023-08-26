from typing import ClassVar
from flair.nn import Classifier
from flair.nn.model import Sentence
from flair.splitter import SegtokSentenceSplitter

# example text
text = "This is a sentence. This is another sentence. I love Berlin."

# initialize the sentence splitter
splitter = SegtokSentenceSplitter()

# use splitter to split text into sentence
sentences = splitter.split(text)

# predict tags for the sentence
tagger = Classifier.load('ner')
tagger.predict(sentences)

for sentence in sentences:
    print(sentence)


from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load_from_file('./best-model.pt')
sentence = Sentence('add your text here for prediction')     # add your text here whose label is to be predicted
classifier.predict(sentence)
print(sentence.labels)
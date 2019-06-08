from flair.embeddings import WordEmbeddings, DocumentPoolEmbeddings, Sentence
from flair.data_fetcher import NLPTaskDataFetcher
from flair.embeddings import  BertEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer
from pathlib import Path
glove_embedding = WordEmbeddings('glove')
bert_embedding = BertEmbeddings('bert-base-uncased')
corpus = NLPTaskDataFetcher.load_classification_corpus(Path('./'), test_file='test.csv', dev_file='dev.csv', train_file='train.csv')
document_embeddings = DocumentPoolEmbeddings([bert_embedding,glove_embedding])
classifier = TextClassifier(document_embeddings, label_dictionary=corpus.make_label_dictionary(), multi_label=True)
trainer = ModelTrainer(classifier, corpus)
trainer.train('./', max_epochs=10)
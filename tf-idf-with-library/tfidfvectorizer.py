import pymysql as mdb

dbConnect = mdb.dbConnect(host="localhost", user="root", passwd="05061996lamongan", db="batik_fix")
cursor = db

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
# ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
print(X.shape)
# (4, 9)

# Tes keberhasilan install flask saja
# from flask import Flask

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
# 	return "Hello World"

# if __name__ == '__main__':
# 	app.run()
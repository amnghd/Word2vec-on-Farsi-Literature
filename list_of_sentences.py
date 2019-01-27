# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 14:47:55 2019

@author: Amin
"""
import re  # for performing a couple of simplae regexes
from gensim.models import Word2Vec  # for performing word2vec training# one note to consider is that "mesra" in farsi poems can be consider as a clause
from time import time  # to monitor the run time

tic = time() # starting time
poems_path = r"poems/"
poet_name = "whole_farsi_corpus.txt"
pattern = re.compile(r"[\n\t]+")  # splitting on tabs or lines (multiples)

with open(poems_path + poet_name, 'r', encoding="utf8") as file:
    raw_string = file.read()  # reading the poet document into a string variable
    raw_string = pattern.sub(raw_string, "\n")# replacing all\n\t with\n to have only mesras
    raw_string = raw_string.replace("[","").replace("]","")  # there are some additional [ and ] that needs to be removed
    unique_chars = set(raw_string) - set("\n\s\t ")  # getting a set of the characters
    mesras = raw_string.split("\n")  # getting a list of mesras(clauses)
    words = re.split(r"[\n\s\t ]+", raw_string)  # getting a list of words
    unique_words = set(words)  # unique words


list_of_sentences = []  # developing a list of sentences to be used for Gsnim
sentence_max_len = 0  # maximum length of the sentences initiaton
sentence_min_len = 100  # minimum length of the sentences initiaton
for mesra in mesras:
    if mesra.strip():  # not an empty line is faced
        mesra_list = [word for word in mesra.strip().split(" ") if word]
        list_of_sentences.append(mesra_list)
        if len(mesra_list) > sentence_max_len:
            sentence_max_len = len(mesra_list)  # developing maximum length of the mesras
        if len(mesra_list) < sentence_min_len:
            sentence_min_len = len(mesra_list)  # developing minimum length of the mesras 
            
            
cache = {}  # to hold informations to be transferred
cache["num_of_uwords"] = len(unique_words)  # caching number of unique words
cache["num_of_chars"] = len(unique_chars)  #cachine number of characarcters
cache["num_of_words"] = len(words) # total number of words
cache["unique_words"] = unique_words  # unique words to be used
cache["sentence_min_max"] = (sentence_min_len, sentence_max_len) #range of mesras in terms of words for troubleshooting
cache["num_mesra"] = len(list_of_sentences) #number of mesras (clauses in this document)

print("There are {} number of mesras in this document.".format(cache["num_mesra"]))
print("Mesra length range from {} words to {} words.".format(sentence_min_len, sentence_max_len))
print("There are {} unique words in this document.".format(cache["num_of_uwords"]))
print("There are {} unique characters in this document.".format(cache["num_of_chars"]))
print("In total there are {} words in this document.".format(cache["num_of_words"]))
# developing the word2vec funtion
model = Word2Vec(
        list_of_sentences,
        size=100,
        window=6,
        min_count=10,
        workers=4)
model.train(list_of_sentences, total_examples=len(list_of_sentences), epochs=10)

# testing if it makes sense
w1 = u'خدا'
print("Few most similar words to \"" + w1 + "\" are:\n" + "\n".join(str(word) +":" + str(ratio) for word, ratio in model.wv.most_similar(positive=w1, topn=10)))

# let's perform an anlogy test between woman, man, adam, and eve
pos1 = u'زن'  # reason
pos2 = u'آدم'
neg = u'مرد'
result = model.wv.most_similar(positive=[pos1, pos2], negative=[neg])
print(neg + u" به " + pos1 + " شبیه " + pos2 + " است:\n{}".format(*result[0]))

# let's perform an anlogy test between ismaeil, ibrahim, hossein, ali
pos1 = u'چشم'  # reason
pos2 = u'شنیده'
neg = u'گوش'
result = model.wv.most_similar(positive=[pos1, pos2], negative=[neg])
print(neg + u" به " + pos1 + " شبیه " + pos2 + " است:\n{}".format(*result[0]))

# saving the vectors 
model.wv.save_word2vec_format(r'word2vec model/farsi_literature_word2vec_model_min50.txt', binary=False)
toc = time()  # end time
delta_time = toc - tic



# now lets perform visualization
#tsne_plot(model)

print("This code takes {} seconds.".format(delta_time))
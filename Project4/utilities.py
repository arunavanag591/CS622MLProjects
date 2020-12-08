
#Arunava Nag; CS 622 Project 4
#!/usr/bin/env python

import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import os
import random


def generate_vocab(dir, min_count, max_files):
  if(max_files == -1):
    #count all files
    path, dirs, pos = next(os.walk(dir+"/pos"))
    path, dirs, neg = next(os.walk(dir+"/neg"))
  
    #check which directory has more number of files
    if (len(pos)) > (len(neg)):
      mx_files = len(neg)
    else:
      mx_files = len(pos)
    
    #check if even number of files
    if (mx_files % 2) == 0:
      fnum = mx_files
    else:
      fnum = mx_files-1  

    # fpos = random.sample(os.listdir(dir+"/pos"), fnum)
    # fneg = random.sample(os.listdir(dir+"/neg"), fnum) 
    #picking first fnum files for consistency
    fpos = os.listdir(dir+"/pos")[:fnum]
    fneg = os.listdir(dir+"/neg")[:fnum] 
  
  else:
    fnum = int(max_files/2) 
    # picking random files
    # fpos = random.sample(os.listdir(dir+"/pos"), fnum)
    # fneg = random.sample(os.listdir(dir+"/neg"), fnum) 
    
    #picking first fnum files for consistency
    fpos = os.listdir(dir+"/pos")[:fnum]
    fneg = os.listdir(dir+"/neg")[:fnum] 
  
  vocab = []
  for filename in fpos:
    with open(dir+"/pos/"+filename) as f:
      #stores all the words from the files from positive
      vocab.append([word for line in f for word in line.split()])

  for filename in fneg:
    with open(dir+"/neg/"+filename) as f:
      #stores all the words from the files from negative
      vocab.append([word for line in f for word in line.split()])
  
  vocab_flat = []
  for sets in vocab:
    for item in sets:
        vocab_flat.append(item)

  #remove special characters and break elements
  result = ["".join(list(filter(str.isalnum, line))) for line in vocab_flat]
  while 'br' in result: result.remove('br')  

  # method slower, higher time complexity
  # vocab_filtered = [ e for e in result if result.count(e) >= min_count]
  
  # method faster
  from collections import Counter
  count_dict = Counter(result)
  vocab_filtered = [el for el in result if count_dict[el]>=min_count]
  
  # final_vocab = list(dict.fromkeys(vocab_filtered))
  final_vocab = list(set(vocab_filtered))
  return final_vocab
  

def create_word_vector(fname, vocab):
  # create vectorizer
  # lamba txt splits every case at space as a word, this includes 
  # all single letter word as I, a to be included as well
  cv = CountVectorizer(tokenizer=lambda txt: txt.split())
  # fit over the vocabulary
  X = cv.fit_transform(vocab)

  with open(fname) as f:
    # read lines
    lines = f.readlines()
    # create vector on new file
    count_list = cv.transform(lines).toarray()

  return count_list



def load_data(dir, vocab, max_files):
  
  fnum = int(max_files/2)
  fpos = os.listdir(dir+"/pos")[:fnum]
  fneg = os.listdir(dir+"/neg")[:fnum] 

  # for printing without truncation
  # nums = np.arange(2000)
  # np.set_printoptions(threshold=sys.maxsize)
  
  positive_vector = []
  for filename in fpos:
      positive_vector.append(create_word_vector((dir+"/pos/"+filename), vocab))
  
  negative_vector = []
  for filename in fneg:
    negative_vector.append(create_word_vector((dir+"/neg/"+filename), vocab))
  
  X = positive_vector + negative_vector
  pos_labels = np.ones(fnum)
  neg_labels = np.ones(fnum)*-1
  Y = np.concatenate((pos_labels,neg_labels), axis = None)

  # test vectorizer
  # cv = CountVectorizer(tokenizer=lambda txt: txt.split())
  # X = cv.fit_transform(['Delhi', 'delhi', 'orange', 'Orange', 'a', 'love', 'And'])
  # count_list = cv.transform(['a LOVE Delhi and Orange']).toarray()
  # print(count_list)
  return X, Y
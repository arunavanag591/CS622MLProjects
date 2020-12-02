
#Arunava Nag; CS 622 Project 4
#!/usr/bin/env python

import numpy
import sklearn
import sys
import os
import random


def generate_vocab(dir, min_count, max_files):
  fnum=int(max_files/2) 
  fpos = random.sample(os.listdir(dir+"/pos"), fnum)
  fneg = random.sample(os.listdir(dir+"/neg"), fnum)
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

  vocab_filtered = []
  # for i in range (len(result)):
  vocab_filtered.append(set(word for word in set(result) if result.count(word) == 1))
  print(len(vocab_filtered))
  print(vocab_filtered)


  # print('\n')
  # print(result)  
  # print(len(vocab_flat))
  # print(vocab_flat)
  

  
  
  
# def create_word_vector(fname, vocab):


# def load_data(dir, vocab, max_files):
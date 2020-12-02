
#Arunava Nag; CS 622 Project 4
#!/usr/bin/env python

import numpy
import sklearn
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

    fpos = random.sample(os.listdir(dir+"/pos"), fnum)
    fneg = random.sample(os.listdir(dir+"/neg"), fnum) 
  
  else:
    fnum = int(max_files/2) 
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

  # method slower, higher time complexity
  # vocab_filtered = [ e for e in result if result.count(e) >= min_count]
  # print(len(vocab_filtered))
  
  # method faster
  from collections import Counter
  count_dict = Counter(result)
  vocab_filtered = [el for el in result if count_dict[el]>=min_count]
  
  return vocab_filtered
  
  
  
# def create_word_vector(fname, vocab):


# def load_data(dir, vocab, max_files):
#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt

def svm_train_multiclass(arr):
    classes = arr [1]
    data = arr[0]
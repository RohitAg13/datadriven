from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from IPython.display import display

from sklearn import metrics


from IPython.lib.deepreload import reload as dreload
import PIL, os, numpy as np, math, collections, threading, json, random, scipy#, cv2
import random, pandas as pd, pickle, sys, itertools, string, sys, re, datetime, time
import seaborn as sns, matplotlib
import IPython, sklearn, warnings,graphviz
#conda install -c anaconda graphviz
from abc import abstractmethod
from glob import glob, iglob
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from itertools import chain
from functools import partial
from collections import Iterable, Counter, OrderedDict
#from isoweek import Week
##conda install -c auto isoweek
#from pandas_summary import DataFrameSummary
from IPython.lib.display import FileLink
from PIL import Image, ImageEnhance, ImageOps
from sklearn import metrics, ensemble, preprocessing
from operator import itemgetter, attrgetter

from matplotlib import pyplot as plt, rcParams, animation
from ipywidgets import interact, interactive, fixed, widgets
matplotlib.rc('animation', html='html5')
np.set_printoptions(precision=5, linewidth=110, suppress=True)

def in_notebook(): return 'ipykernel' in sys.modules

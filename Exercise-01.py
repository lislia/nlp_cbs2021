#!/usr/bin/env python
# coding: utf-8

# # Exercise on Regular Expressions
# 

# ### Q.No: 1. RegexOne Tutorial  
# 
# Go to: https://regexone.com/lesson/introduction_abcs and familiarise your self with the regular expression syntax by completing the tutorial. Complete all the 15 tutorials without looking into solution. If you get stuck and even after discussing with others, if you dont get answer, then you may look into the solution. 
# 
# 

# ## Q.No: 2
# 
# In the following example, you have a list containing the information about people in the form of 
# [lastname], [firstname]; [emailaddress]; [telephone number]
# 
# A) Use regular expressions in Python to extract information from the list and display in the following format:
# 
#     [firstname] [lastname] : [CBS username]
# For example, the first record should be displayed as:
# 
#      Raghava Mukkamala : rrm.itm    
# 
# B) Use regular expressions in Python to extract the name and telephone information from the list and display in the following format:
# 
#     [firstname] [lastname] : [Telephone Nmber without country code]
#     
# For example, the first record should be displayed as:
# 
#     Raghava Mukkamala : 41852299    
# 
# Hint: You can see some code examples about using regular expressions in Python.
# https://regexone.com/references/python
# 

# In[14]:


# Example to extract user ids form the contact information.

import re
contactInfo = ['Mukkamala, Raghava; rrm.itm@cbs.dk; +4541852299', 
'Vatrapu, Ravi; rv.itm@cbs.dk; 24794315', 
'Hussain, Abid; ah.itm@cbs.dk; +4538154478', 
'Lasrado, Lester; lal.itm@cbs.dk; +4538155668']


# ## Q.No:3 Install the following packages   
# 
# 1) Natural Language Toolkit (NLTK) along with NLTK Data
#     More info: https://www.nltk.org/
# 
# 2) TextBlob: Simplified Text Processing 
#     More info: https://textblob.readthedocs.io/en/dev/
# 
# 3) spaCy Industrial-Strength Natural Language Processing in Python 
#     More info: https://spacy.io/
# 
# 4) prettytable Package for showing the results in pretty tabular format.
# 
# You can use pip to install these packages.
# 
# Hint 
# 1) First install NLTK, before installing TextBlob, as TextBlob internally uses NLTK.
# 
# 2) : If you get problems in loading spacy, to fix an error: spacy.load('en_core_web_sm') error, use the following command.
# 
# pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz#egg=en_core_web_sm

# ## Q.No: 4 Tokenization using Textblob
# 
# Use the textblob package to split the doc1 into a) sentenses and b) tokens and dsiplay them in tabular format.
# 

# In[15]:


from textblob import TextBlob
from prettytable import PrettyTable

doc1 ="""
A. A. Milne: The third-rate mind is only happy when it is thinking 
with the majority. The second-rate mind is only happy 
when it is thinking with the minority. 
The first-rate mind is only happy when it is thinking.
"""



# ## Q.No: 5 Entity Recognition and POS Tagging 
# 
# Use NLTK, spcay libraries to do POS tagging and Entity recontion and compare the results.
# 
# Hint: You can look into this blog for more information. https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da
# 
# 

# In[16]:


import nltk
import spacy


text1 = "Apple is looking at buying U.K. startup for $1 billion"


# In[ ]:





# ## Q.No: 6 Stemming and Lemmatization
# 
# Use the nltk and spacy packages to compare the lemmas of the words from the following sentenses and compare the results.
# 
# Hint: Take some famous quotes from: https://www.brainyquote.com/topics/famous and try the both 
# NLTK and spacy to see which one performs better.

# In[18]:


textdoc = "Mark Twain: Twenty years from now you will be more disappointed"+ "by the things that you didn’t do than by the ones you did do."



# ## Q.No: 7 Edit Distances
# 
# In the following code, you are given a list of words starting with 'l' and a misspelt word.
# Compute the edit distances between the misspelt word and the words in the list and find out
# A) which word is the closest word
# B) which word is the farthest word 
# 
# You can comapute the edit distances both with a) cost of substitution = 1 b) cost of substitution = 2. 
# 

# In[23]:


import nltk
from prettytable import PrettyTable


list_words = [ 'little', 'leader', 'likely', 'living', 'latest', 'letter',               'league', 'listen', 'launch', 'length', 'latter', 'leaves',               'linked', 'losing', 'labour', 'lights', 'liquid', 'legacy',               'lucent', 'luxury', 'lawyer', 'lesson', 'lovely', 'lesser',               'loaded', 'linear', 'landed', 'locate', 'liable', 'layout',               'loving', 'legend', 'lively', 'lounge', 'lonely', 'lately',               'ladder', 'lining', 'lethal', 'legion', 'liquor', 'locker',               'litter', 'latent', 'lavish', 'ledger', 'laurel']

#print(len(list_words))

misspeld_word = 'lxuruy'


# In[ ]:





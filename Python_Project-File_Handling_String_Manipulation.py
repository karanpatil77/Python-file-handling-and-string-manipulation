#!/usr/bin/env python
# coding: utf-8

# Task1 - Find out the number of unique characters in the sample conversation

# In[13]:


import pandas as pd
import numpy as np


# In[14]:


a = []
f = open('D:/Internshala/python/DSProject/conv.txt','r').readlines()
# print each line text
for line in f :
    unique_characters = line.split(' ')
    if unique_characters[0] != '\n':
        if unique_characters[0].endswith(':') == 1:
            a.append(unique_characters[0].replace(":",""))
        else:
            c = (unique_characters[0] + " " +unique_characters[1])
            a.append(c.replace(":",""))
b=set(a)
print("No of unique characters involved in the conversation are :- ",len(b),"\nThose are :- ")
b


# In[15]:


# Opening the text file and storing its contents in a list stored_conv
with open("D:/Internshala/python/DSProject/conv.txt") as f:
    conv = f.read()

# splitting the list contents with the parameter \n to make unique list elements by creating a list order
temp_list = list(conv.split('\n'))
temp_list


# Task 2 - Create a new text file for each of the characters with their name and store the unique words
# said by them in their respective file. Store one word in one line.

# In[16]:


# creating a function to remove the punctuation marks within the dialouges

def remove_punctuation(string):
    punctuation = "''.,!?..."
    clean_text = ''.join(ch for ch in string if ch not in punctuation)
    return (clean_text)


# In[17]:


updated_list = [] 
for i in range(len(temp_list)):
    updated_list.append(remove_punctuation(temp_list[i]))  
updated_list


# In[18]:


# Creating a list for storing the name of the characters as well as storing the individual dialogues of the characters

name_of_character = []
dialogues_WILL = []
dialogues_WAYMAR = []
dialogues_GARED = []
dialogues_ROYCE = []
dialogues_JON = []
dialogues_SEPTA = []
dialogues_SANSA = []
dialogues_NED = []
dialogues_ROBB = []
dialogues_CASSEL = []
dialogues_CATELYN = []
dialogues_BRAN = []
dialogues_THEON = []
dialogues_CERSEI = []
dialogues_JAIME = []
dialogues_ROBERT = []
dialogues_ARYA = []


# In[19]:


# main logic of code

for i  in range(len(updated_list)):                                 # traversing the complete list of the text stored 
    if updated_list[i] == '':
        continue
    else:
        name_of_character.append(updated_list[i].split(':')[0])     # storing the names of the characters
        if name_of_character[-1] == 'WILL':
            for word in updated_list[i].split(':')[1].split():      # splitting the dialogue of an individual character
                if word not in dialogues_WILL:                      # in this case, we are splitting the dialogue said by WILL
                    dialogues_WILL.append(word)                     # then we append the said words in the list if the words
            with open('WILL.txt' , mode = 'w') as f:                    # said are not already present in the list
                for word in dialogues_WILL:                         # then we write them down in a text file with the characters name
                    f.write(word)
                    f.write('\n')
                    
        elif name_of_character[-1] == 'ARYA':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_ARYA:
                    dialogues_ARYA.append(word)
            with open('ARYA.txt' , mode = 'w') as f:
                for word in dialogues_ARYA:
                    f.write(word)
                    f.write('\n')
                    
        elif name_of_character[-1] == 'BRAN':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_BRAN:
                    dialogues_BRAN.append(word)
            with open('BRAN.txt' , mode = 'w') as f:
                for word in dialogues_BRAN:
                    f.write(word)
                    f.write('\n')            
                    
        elif name_of_character[-1] == 'WAYMAR ROYCE':               # We do the same likewise to all other the Characters 
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_WAYMAR:
                    dialogues_WAYMAR.append(word)
            with open('WAYMAR ROYCE.txt' , mode = 'w') as f:
                for word in dialogues_WAYMAR:
                    f.write(word)
                    f.write('\n')
                    
        elif name_of_character[-1] == 'CASSEL':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_CASSEL:
                    dialogues_CASSEL.append(word)
            with open('CASSEL.txt' , mode = 'w') as f:
                for word in dialogues_CASSEL:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'CATELYN':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_CATELYN:
                    dialogues_CATELYN.append(word)
            with open('CATELYN.txt' , mode = 'w') as f:
                for word in dialogues_CATELYN:
                    f.write(word)
                    f.write('\n')                    
                    
        elif name_of_character[-1] == 'GARED':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_GARED:
                    dialogues_GARED.append(word)
            with open('GARED.txt' , mode = 'w') as f:
                for word in dialogues_GARED:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'ROYCE':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_ROYCE:
                    dialogues_ROYCE.append(word)
            with open('ROYCE.txt' , mode = 'w') as f:
                for word in dialogues_ROYCE:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'JON':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_JON:
                    dialogues_JON.append(word)
            with open('JON.txt' , mode = 'w') as f:
                for word in dialogues_JON:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'SEPTA MORDANE':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_SEPTA:
                    dialogues_SEPTA.append(word)
            with open('SEPTA MORDANE.txt' , mode = 'w') as f:
                for word in dialogues_SEPTA:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'SANSA':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_SANSA:
                    dialogues_SANSA.append(word)
            with open('SANSA.txt' , mode = 'w') as f:
                for word in dialogues_SANSA:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'NED':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_NED:
                    dialogues_NED.append(word)
            with open('NED.txt' , mode = 'w') as f:
                for word in dialogues_NED:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'ROBB':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_ROBB:
                    dialogues_ROBB.append(word)
            with open('ROBB.txt' , mode = 'w') as f:
                for word in dialogues_ROBB:
                    f.write(word)
                    f.write('\n')

        elif name_of_character[-1] == 'THEON':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_THEON:
                    dialogues_THEON.append(word)
            with open('THEON.txt' , mode = 'w') as f:
                for word in dialogues_THEON:
                    f.write(word)
                    f.write('\n')
                    
        elif name_of_character[-1] == 'CERSEI':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_CERSEI:
                    dialogues_CERSEI.append(word)
            with open('CERSEI.txt' , mode = 'w') as f:
                for word in dialogues_CERSEI:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'JAIME':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_JAIME:
                    dialogues_JAIME.append(word)
            with open('JAIME.txt' , mode = 'w') as f:
                for word in dialogues_JAIME:
                    f.write(word)
                    f.write('\n')
        
        elif name_of_character[-1] == 'ROBERT':
            for word in updated_list[i].split(':')[1].split():
                if word not in dialogues_ROBERT:
                    dialogues_ROBERT.append(word)
            with open('ROBERT.txt' , mode = 'w') as f:
                for word in dialogues_ROBERT:
                    f.write(word)
                    f.write('\n')
   
        
        else:
            continue


# In[ ]:





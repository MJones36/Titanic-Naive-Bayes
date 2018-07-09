
# coding: utf-8

# # Titanic - Naive Bayes

# Using the Titanic dataset and Bayes Theorem, I found out which of the following individuals is more likely to survive: a boy in 2nd class class, a woman in 3rd class or a man in 1st class.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


location = "titanic.xls"
df = pd.read_excel(location)
df.head()


# In[6]:


#gather all features
df_survive = df[df['survived'] == 1] #all survivors
df_boy2 = df[(df['sex'] == 'male') & (df['age'] < 18)] #boys 
df_women3 = df[(df['sex'] == 'female') & (df['age'] >= 18)] #women 
df_men1 = df[(df['sex'] == 'male') & (df['age'] >= 18)] #men  

df_2class = df[df['pclass'] == 2] #2nd class
df_3class = df[df['pclass'] == 3] #3rd class
df_1class = df[df['pclass'] == 1] #1st class


# In[15]:


#probability of features

p_survive = len(df_survive) /len(df) #survivors
p_boy = len(df_boy2) /len(df) #boys
p_women = len(df_women3) / len(df) #women
p_men = len(df_men1) /len(df) #men

p_2class = len(df_2class)/len(df) #2nd class
p_3class = len(df_3class)/len(df) #3rd class
p_1class = len(df_1class)/len(df) #1st class


# In[16]:


#conditional features
df_survboy = df_survive[(df['sex'] == 'male') & (df['age'] < 18)] #boys that survived
df_survwomen = df_survive[(df['sex'] == 'female') & (df['age'] >= 18)]
df_survmen = df_survive[(df['sex'] == 'male') & (df['age'] >= 18)] 

df_surv2class = df_survive[df['pclass'] == 2] #2nd class survivors
df_surv3class = df_survive[df['pclass'] == 3] #1st class survivors
df_surv1class = df_survive[df['pclass'] == 1] #3rd class survivors


# In[17]:


#probability of conditional features give that they will survived

p_survboy = len(df_survboy)/len(df_survive)
p_survwomen = len(df_survwomen)/len(df_survive)
p_survmen = len(df_survmen)/len(df_survive)

p_surv2class = len(df_surv2class)/len(df_survive)
p_surv3class = len(df_surv1class)/len(df_survive)
p_surv1class = len(df_surv3class)/len(df_survive)


# In[21]:


#probability of surival given features

p_survB2 = ((p_survive)* p_survboy * p_surv2class)/(p_boy * p_2class)
p_survW3 = ((p_survive)* p_survwomen * p_surv3class) / (p_women * p_3class)
psurvM1 = ((p_survive)* p_survmen * p_surv1class) / (p_men * p_1class)


# In[25]:


#probability of a boy in 2nd class surviving
print(p_survB2*100)


# In[26]:


#probability of a woman in 3rd class surviving
print(p_survW3*100)


# In[27]:


#probability of a man in 1st class surviving
print(psurvM1*100)


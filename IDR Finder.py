#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import regular expression and pandas
import re
import pandas as pd

#define a new function taking in an amino acid sequence string, searching for
#possible intrinsically disordered regions and returning all these disordered  
#patterns in a list
def find_IDR (string):
    outcome = [];
    outcome += re.findall(r"[SYT]Y[A-Z]{2}[VILMFWC]", string);
    outcome += re.findall(r"P[TS]AP",string);
    outcome += re.findall(r"[VILMFWC][A-Z]{2,3}[VILMFWC][A-Z]{2,3}[VILMFWC][A-Z][VILMFWC]",string);
    # Differentiate YXXΦ from pYXXΦ, prevent from repetitive countings.
    if re.findall(r"[^SYT]Y[A-Z]{2}[VILMFWC]",string) != False:
        temp = re.findall(r"[^SYT]Y[A-Z]{2}[VILMFWC]",string);
        for e in temp: 
            e = e[1:len(e)];
        outcome += temp;
    outcome += re.findall(r"Q[A-Z]{2}[VILMFWC][A-Z]{2}[FHT][FHY]",string);
    outcome += re.findall(r"[ST][A-Z][IL]P",string);
    outcome += re.findall(r"[RK][A-Z]L[A-Z]{0,1}[VILMFWC]",string);
    outcome += re.findall(r"P[A-Z]I[A-Z][IV]",string);
    outcome += re.findall(r"R[A-Z]{2}L[A-Z]{2}[VILMFWC]",string);
    outcome += re.findall(r"[SYT][ST]P[A-Z]{2}[SYT][ST]",string);
    outcome += re.findall(r"[VILMFWC]K[A-Z][DE]",string);
    outcome += re.findall(r"[DE][A-Z][ST][VILMFWC]",string);
    outcome += re.findall(r"[DE][A-Z]{2}D[GSAN]",string);
    outcome += re.findall(r"[SYT][ST]P",string);
    return outcome;

#read in a csv file and output a new csv file with Entry and IDR patterns
data = pd.read_csv('Actin Proteins.csv')
data_Frame = pd.DataFrame()
data_Frame['Entry'] = data['Entry']
data_Frame['IDR'] = data['Sequence'].apply(find_IDR)
data_Frame.to_csv("output.csv")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[68]:


#import regular expression and pandas
import re
import pandas as pd

#define a new function taking in an amino acid sequence string, searching for
#possible intrinsically disordered regions and returning all these disordered  
#patterns in a list

def find_IDR (string):
    outcome = [];
    index = [];
    All_pattern = [r"[SYT]Y[A-Z]{2}[VILMFWC]",r"P[TS]AP",r"[VILMFWC][A-Z]{2,3}[VILMFWC][A-Z]{2,3}[VILMFWC][A-Z][VILMFWC]",
                   r"Q[A-Z]{2}[VILMFWC][A-Z]{2}[FHT][FHY]",r"[ST][A-Z][IL]P",r"[RK][A-Z]L[A-Z]{0,1}[VILMFWC]",
                   r"P[A-Z]I[A-Z][IV]",r"R[A-Z]{2}L[A-Z]{2}[VILMFWC]",r"[SYT][ST]P[A-Z]{2}[SYT][ST]",r"[VILMFWC]K[A-Z][DE]", 
                   r"[DE][A-Z][ST][VILMFWC]",r"[DE][A-Z]{2}D[GSAN]",r"[SYT][ST]P"];
    for n in All_pattern:
        outcome += re.findall(n,string);
        #outcome += re.finditer(n,string).span();
    if re.findall(r"[^SYT]Y[A-Z]{2}[VILMFWC]",string) != False:
        temp = re.findall(r"[^SYT]Y[A-Z]{2}[VILMFWC]",string);
        for e in temp: 
            e = e[1:len(e)];
        outcome += temp;
        #outcome += re.finditer().span();
    for i in outcome:
        index += [m.span() for m in re.finditer(i, string)];
    return pd.Series([outcome, index]);

#read in a csv file and output a new csv file with Entry and IDR patterns


data = pd.read_csv('Actin Proteins.csv');
data_Frame = pd.DataFrame();
data_Frame['Entry'] = data['Entry'];
data_Frame[['IDR','Index']]= data['Sequence'].apply(find_IDR);
data_Frame.to_csv("output.csv");


# In[ ]:




    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_option_menu import option_menu

import json
import requests
import pandas as pd
import numpy as np


from io import StringIO
import langdetect
from langdetect import DetectorFactory, detect, detect_langs
from PIL import Image
logo = Image.open('./media/logo.png')

st.set_page_config(
    page_title="MP4 Findings",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:tdi@cphbusiness.dk',
        'About': "https://docs.streamlit.io"
    }
)

st.sidebar.header("Try Me!", divider='rainbow')
# st.sidebar.success("Select a demo case from above")
st.image(logo, width=200)

banner = """
    <body style="background-color:yellow;">
            <div style="background-color:#385c7f ;padding:10px">
                <h2 style="color:white;text-align:center;">MP4 Assignment</h2>
            </div>
    </body>
    """

st.markdown(banner, unsafe_allow_html=True)


st.markdown(
    """
### Which machine learning methods did you choose to apply in the application?
We used Decision tree classifier.
""")
st.markdown("---")

st.markdown("""
### How accurate is your solution of prediction?
- Decision Tree Classifier:
- Accuracy: 0.8163
- Confusion Matrix:

[[221  34]
[ 20  19]]

- Classification Report:

0 precision: 0.92   recall: 0.87  f1-score: 0.89   support: 255

1 precision: 0.36   recall: 0.49  f1-score: 0.41   support: 39

accuracy:                         f1-score: 0.82   support: 294

macro avg: precision: 0.64     recall: 0.68  f1-score: 0.65   support: 294

weighted avg: precision:  0.84    recall: 0.82  f1-score: 0.83   support: 294

""")
st.markdown("---")

st.markdown("""
### Which are the most decisive factors for quitting a job?
The most deciding factors for quitting the job seems to be 
Overtime work, Marital status, TotalWorkingYears, and JobLevel showcased by the correlation matrix. 
""")
st.image('media/correlationmatrix.png')
st.markdown("---")

st.markdown(
"""
### Which work positions and departments are in higher risk of losing employees?
The Sales department seems to be the department with highest risk of losing employees, with the Sale Representative Job role being the highest risk.

""")
st.image('media/AttritionInDepartment.png')
st.markdown("---")


st.markdown("""
### Are employees of different gender paid equally in all departments?
It seems to very equal across the board. The differences seem very small and in some of the jobs the women have higher average, while in others the men have higher average. Both by small margins.

""")
st.image('media/GenderPay.png')
st.markdown("---")

st.markdown("""
### Do the family status and the distance from work influence the work-life balance?
They do not seem to show a strong corrolation no.
DistanceFromHome vs WorkLifeBalance corrolation coefficient is -0.026556, indicating a weak negative relationship.

As for marital status:
Divorced correlation coefficient is -0.009080, showing a very weak negative relationship with worklifebalance.         
Married correlation coefficient is -0.006388, again showing a very weak negative relationship with worklifebalance.  
Single correlation coefficient is 0.014921, this time showing a very weak positive relationship with worklifebalance.

This all in all seems to indicate there doesn't seem to be a strong correlation between either marital status or distance from work.


""")
st.markdown("---")


st.markdown("""
### Does education make people happy (satisfied from the work)?
Education and JobSatisfaction seems to be similar across the board with every education level having JobSatisfaction 3 or 4 being the highest value. 
However, it should be noted that in Education level 5, JobSatisfaction being 1 is nearly as high as 3 and 4.
To answer the question bluntly: No, higher education does not indicate to make people happy in this case.

""")
st.image('media/JobSatisfactionVSEducation.png')
st.markdown("---")


st.markdown("""
### Which were the challenges in the project development?
Mainly Streamlit. It was really hard to figure out how to make it work and it was running veeeeery slowly for some reason, so testing the inbuilt user input stuff took incredibly long time. 
"""
)


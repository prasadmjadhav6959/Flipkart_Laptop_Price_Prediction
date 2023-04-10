import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.header('Flipkart Laptop Price Prediction')

company = st.selectbox('Brand Name',df['Brand Name'].unique())

Os = st.selectbox('Operating System',df['OS'].unique())

# ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])
ramtype = st.selectbox('RAM Type',df['Ram Type'].unique())


ram = st.selectbox('RAM Size',df['RAM'].unique())

processor = st.selectbox('Processor',df['Processor'].unique())

gpu = st.selectbox('GPU',df['GPU'].unique())

warr = st.selectbox('Warranty',df['Warranty'].unique())

screensize = st.selectbox('Screen Size',df['ScreenSize'].unique())

disktype = st.selectbox('Disk Type',df['Disk Type'].unique())

disksize = st.selectbox('Disk Size',df['DISK SIZE'].unique())

if st.button('Predict'):
    
    query = np.array([company,Os,ramtype,ram,processor,gpu,warr,screensize,disktype,disksize])
    query = query.reshape(1,10)
    # st.title(pipe.predict(query))
    
    # st.title("Laptop Predicted Price is ₹ " + str(int(np.exp(pipe.predict(query)[0]))))
    st.subheader('Laptop Predict Price ₹ ' + str(int(pipe.predict(query)[0])))

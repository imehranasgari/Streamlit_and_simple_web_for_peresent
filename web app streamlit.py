import streamlit as st
import numpy as np 
import pandas as pd 

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# ...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# ...     \sum_{k=0}^{n-1} ar^k =
# ...     a \left(\frac{1-r^{n}}{1-r}\right)
# ...     ''')'''
'''df=pd.read_csv('C:/Users/pc/Downloads/Video/app/googleplaystore.csv')
st.dataframe(df)

from PIL import Image
photo=Image.open('C:/Users/pc/Downloads/Video/OIP.jpg') 
st.image(photo)   '''

'''import time
my_bar=st.progress(0)
with st.spinner('Wait for it...'):
    for my_time in range(100):
        time.sleep(0.05)
        my_bar.progress(my_time + 1)'''

'''st.success('Done!')'''

st.sidebar.header('user iput value')

def user_featture_input ():
    sepal_length=st.sidebar.slider('sepal_length', 4.3, 7.9, 5.4)
    sepal_width=st.sidebar.slider('sepal_width',2.0, 4.4, 3.4)
    petal_length=st.sidebar.slider('petal_length',1.0, 6.9, 1.3)
    petal_width=st.sidebar.slider('petal_width',0.1, 2.5, 0.2)
    data={'sepal_length':sepal_length,
          'sepal_width':sepal_width,
          'petal_length':petal_length,
          'petal_width':petal_width}
    feature_user=pd.DataFrame(data,index=[0])
    return feature_user

df=user_featture_input()

st.subheader('user input value')
st.write(df)

ires_data=datasets.load_iris()
X=ires_data.data
Y=ires_data.target

st.header('class')
st.write(ires_data.target_names)


clf=RandomForestClassifier()
clf.fit(X,Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediction')
st.write(ires_data.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

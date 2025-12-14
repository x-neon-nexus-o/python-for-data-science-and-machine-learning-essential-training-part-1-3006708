import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

col_names = ["column1", "column2", "column3"]

data = pd.DataFrame(np.random.randint(30,size=(30,3)), columns=col_names)

st.line_chart(data)
st.bar_chart(data)

animals=["dog","cat","fish","bird","tiger","lion","elephant","giraffe"]
height=[30,25,10,15,40,45,50,55]

fig,ax=plt.subplots()
ax.pie(height,labels=animals)

st.pyplot(fig)
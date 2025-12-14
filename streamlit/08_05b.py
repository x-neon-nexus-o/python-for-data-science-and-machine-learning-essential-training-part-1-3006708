import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Sales Data Analysis")
animals=['Cat', 'Dog', 'Rabbit', 'Hamster', 'Parrot']
heights = [23, 17, 35, 29, 12]
weight=[ 6, 8, 4, 3, 1]


fig,ax=plt.subplots()

x=np.arange(len(animals))
width=0.40

ax.bar(x-0.2, heights,width, color="red")
ax.bar(x+0.2, weight,width, color="blue")


ax.legend(["Height", "Weight"])
ax.set_xticks(x)
ax.set_xticklabels(animals)


st.pyplot(fig)

st.write("This bar chart compares the heights and weights of different animals.")
st.write("Red bars represent heights and blue bars represent weights.") 
st.write("You can customize the data and colors as needed for your analysis.")

explode=[0.2,0.1,0.1,0.1,0.1]
plot_pie,ax=plt.subplots()
ax.pie(heights,explode=explode,labels=animals,autopct="1.1f%%",shadow=True)
ax.axis("equal")
st.pyplot(plot_pie)

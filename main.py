import streamlit as st #used to deploy apps in ashort period of time
import pandas #create quick data diagram

data={
  'Series_1':[1,2,3,4,5],
  'Series_2':[10,20,30,40,50]
}

df=pandas.DataFrame(data)

st.title("Creating a website using streamlit")
st.subheader('Demonstration of how quick it is to deploy an app')
st.write("We will be using streamlit in order to deploy our website faster in the cloud.")
st.write(df)
st.line_chart(df)
st.area_chart(df)

my_slider=st.slider('Celsius')
st.write(my_slider, 'in Fahrenheit is: ', my_slider *9/5 +32)
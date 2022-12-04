import streamlit as st
import numpy as np
import pandas as pd 
import pickle

model = pickle.load(open('cloth_size_classifier.pkl','rb'))

st.title("Cloth Size Prediction")

first,last = st.columns(2)
third,fourth= st.columns(2)

val1=first.number_input("Age",4,100)
val2=last.number_input("Height (cm)",80,300)
val3=third.number_input("Weight (cm)",5,200)
gender=['Male','Female']
val4=fourth.radio("Gender:",gender)

if val4 == 'Male':
    val4=1
if val4 == "Female":
    val4=0

inputdata = pd.DataFrame(data=[[val1,val2,val3,val4]],columns=['age',"height",'weight','sex'])
predict = st.button("Predict")
if predict:
    pred = model.predict(inputdata)[0]
    if pred == 1:
        st.write("Your predicted cloth size is: XXS")
    if pred == 2:
        st.write("Your predicted cloth size is: S")
    if pred == 3:
        st.write("Your predicted cloth size is: M")
    if pred == 4:
        st.write("Your predicted cloth size is: L")
    if pred == 5:
        st.write("Your predicted cloth size is: XL")
    if pred == 6:
        st.write("Your predicted cloth size is: XXL")
    if pred == 7:
        st.write("Your predicted cloth size is: XXXL")

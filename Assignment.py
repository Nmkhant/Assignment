import streamlit as st
import numpy as np
import pandas as pd
import math

calories = st.empty()
n = 0
weight = []
height = []
BMI=0
gender = ()
behavior = []
behavior_value = 0
age = 0

def F_calories(n):                        #Calculate Female Calories 
    calories = (user_weight*4.35)+(user_height*4.7)
    calories += 655
    calories -= age*4.7
    calories *= n
    calories = math.ceil(calories)
    st.write("The Average Calories Needed Per Day To You is:" , calories)


    
def M_calories(n):                          #Calculate Male Calories
    calories = (user_weight*6.23)+(user_height*12.7)
    calories += 66
    calories -= age*6.8
    calories *= n
    calories = math.ceil(calories)
    st.write("The Average Calories Needed Per Day To You is:" , calories)

st.title("Fit With My App")

st.subheader("Here You Can Calculate Your BMI And Calories Needed Per Day")


for i in range (0,300):                     #get user_weight
    weight.append(i)
user_weight = st.selectbox('Please Give Me Your Weight In Pounds:' , weight)
'Your Weight:',user_weight , 'lb'


for i in range (0,84):                       #get user_height
    height.append(i)
user_height = st.selectbox('Please Give Me Your Height In Inches:' , height)
'Your Height:',user_height , 'inches'


if user_weight and user_height:                     #calculate BMI and estimate weight level
    input_weight = (user_weight/2.2)
    input_height = (user_height*user_height)*0.0006
    BMI = input_weight / input_height
    'Your BMI is:' , math.ceil(BMI)
    if BMI<18.5:
        st.write("You are Underweight.")
    elif 18.5<BMI<24.9:
        st.write("You are NormalWeight.")
    elif 25.0<BMI<29.9:
        st.write("You are Overweight.")



gender= st.radio("What is your Gender?" , ['Male' ,'Female'])              #get user_gender


age = st.slider("Select Your Age", 0 , 100)                              #get user_age
'Your age is:' , age


behavior = st.radio('Do You Ever Do Exercise?' ,                        #get user_behavior
                      ['No Exercise ever',
                      'Exercise 1-3 Days Per Week',
                      'Exercise 3-5 Days Per Week',
                      'Exercise 6-7 Days Per Week',
                      'I am a Body Builder'])


if behavior == 'No Exercise ever':
    behavior_value = 1.2
elif  behavior == 'Exercise 1-3 Days Per Week':
    behavior_value = 1.25
elif behavior ==  'Exercise 3-5 Days Per Week':
    behavior_value = 1.55
elif behavior ==  'Exercise 6-7 Days Per Week':
    behavior_value = 1.725
else:
    behavior_value = 1.9


column1 , column2 = st.columns(2)                               #output user_calories
pressed = column1.button("Calculate Calories")
if pressed:
    if gender == "Female":
        F_calories(behavior_value)
    elif gender == "Male":
        M_calories(behavior_value)
else:
    column2.write("The Average Calories Needed Per Day To You is 0")

    
st.write('Note*: You must average burn 500 Calories per day by doing exercise or eat less 500 calories per day to lose 1pound in a week.Otherwise, You will average need more 500 Calories per day to gain 1pound in a week.')


st.write('"Stay Healthy , Stay Strong"')
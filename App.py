import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
from PIL import Image

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score




stroke=pd.read_csv("stroke.csv")
heartdisease=pd.read_csv("heartdisease.csv")
lungcancer=pd.read_csv("lungcancer.csv")


st.markdown("# !!!! Welcome to my website !!!!")
col1,col2,col3=st.columns([1,2,1])

logo = Image.open('msu_logo.png')
col1.image(logo, caption='MSU')

egr = Image.open('msu.png')
egr= egr.resize((1000, 1000))
col3.image(egr, caption='Spartans')

st.sidebar.write("My github link: [link](https://github.com/binsarda/CMSE-830-Mid-term-Project)")
cmse= Image.open('cmse.jfif')

st.sidebar.image(cmse, caption='CMSE')

col1,col2,col3=st.columns([1,2,1])
col1.write("Owner Name: Sardar Nafis Bin Ali")
col3.write("Institution: Michigan State University")
with st.expander(  "# Click here to know about author of this site!"):
    nafispic = Image.open('nafis.jpg')
    st.image(nafispic, caption='Sardar Nafis Bin Ali')
    st.write("Sardar is driven by a thirst for knowledge and has a spirit of exploration. "
             "He focused on the captivating domain of high-speed aerodynamics during his undergraduate "
             "studies in mechanical engineering. Currently, he is pursuing "
             "a Ph.D. in mechanical engineering and planning to do a dual"
             " degree with the department of communicative sciences and "
             "disorders. He aims to learn about the intricate aspects of"
             "human communication and contribute to advancements in voice science."
             " Apart from his academic pursuits, he finds solace in traveling, "
             "embracing diverse cultures, and capturing the world's beauty through "
             "his experiences. Sardar actively engages in initiatives "
             "promoting sustainability and environmental conservation. "
             "With an unquenchable curiosity and unwavering dedication, "
             "he continues to make a meaningful impact in his chosen fields and beyond.")

visitor_name=st.text_input("Enter your name:"," ")
st.write("Thank you",visitor_name,", for visiting my website.")
st.markdown("Here you can find datasets related to serious diseases.")
st.write("There are 3 datsets-")
st.markdown("*")
st.write("1. Heart Disease")
st.markdown("*")
st.write("2.Lungs Cancer")
st.markdown("*")
st.write("3.Brain Stroke")
st.markdown("*")





data_button=st.selectbox('Please select one dataset from the following:',['Brain Stroke','Lungs Cancer','Heart Disease'])

if data_button == 'Brain Stroke':
    df1 = stroke
    st.write("You have selected 'Brain Stroke' Dataset")
elif data_button=='Heart Disease':
    df1=heartdisease
    st.write("You have selected 'Heart Disease' Dataset")
elif data_button=='Lungs Cancer':
    df1 = lungcancer
    st.write("You have selected 'Lungs Cancer' Dataset")


status=False
file_button=st.radio('Do you want your own dataset to upload', ['No', 'Yes'])
if file_button=='Yes':
    uploaded_file = st.file_uploader("Choose a CSV file")
    try:
        pd.read_csv(uploaded_file.name)
        status=True
    except:
        status=False
        st.write("File reading not successful")
    if status:
        st.write(f"You uploaded your file successfully and name of your uploaded file is: {uploaded_file.name}")
        df1=pd.read_csv(uploaded_file.name)


button=st.radio('Do you want to delete any row having NaN in at least one of the fields', ['Yes', 'No'])
if button=='Yes':
    df=df1.dropna()
    st.write("You deleted rows having NaN in at least one of the fields")
elif button=='No':
    df = df1
st.write(df.head(12))
col1,col2,col3=st.columns([2,1,2])
button1=col1.button("Show Statistics")
if button1:
    st.sidebar.write(df.describe())

if col3.button("Hide Statistics"):
    button1=False

cols=df.columns
numcols= df.select_dtypes(include=[np.number]).columns
strcols=df.select_dtypes(include=['object']).columns



col1,col2,col3=st.columns([2,1,2])
button2=col1.button("Show Columns")
if button2:
    st.sidebar.write("No. of columns are ",len(cols))
    st.sidebar.write("The columns are following-")
    st.sidebar.write(df.columns)
    st.sidebar.write("Name of columns containing numerical values: ")
    st.sidebar.write(numcols)
    st.sidebar.write("Name of columns containing string or non-numerical values: ")
    st.sidebar.write(strcols)
if col3.button("Hide Columns"):
    button2=False
st.write("Please select following variables for different plotting")
xv=st.selectbox('Please select x or first variable:',cols)
yv=st.selectbox('Please select y or second variiable:',cols)
zv=st.selectbox('Please select hue or third variiable:',cols)

button3=st.button("Bar Chart");
if button3:
    st.bar_chart(data=df, x=xv, y=yv)

if st.button("Hide Bar Chart"):
    button3=False

button4=st.button("Heat Map");
if button4:
    heatmap_fig = px.density_heatmap(df, x=xv, y=yv, marginal_x="histogram", marginal_y="histogram")
    st.plotly_chart(heatmap_fig, theme=None)

if st.button("Hide Heat Map"):
    button4=False

st.write("Done until this!!!")



st.write("Please select reduced number of columns for Reduced Dataset (Select at least 3 variables (at least 2  of numerical type"
         " and at least one  of string or non-numerical type))")
red_cols=st.multiselect('Pick the columns', cols)



if len(red_cols)>0:
    red_df = df[red_cols]
    st.write(
        f"You have choosen {len(red_cols)} number of columns in datatset and number of different column is {len(red_cols)} ")
    st.write("Reduced Dataset")
    st.write(red_df.head(10))
    red_numcols = red_df.select_dtypes(include=[np.number]).columns
    red_strcols = red_df.select_dtypes(include=['object']).columns
    st.sidebar.write("For reduced dataset")
    st.sidebar.write("No. of columns are ", len(red_cols))
    st.sidebar.write("The columns are following-")
    st.sidebar.write(red_df.columns)
    st.sidebar.write("Name of columns containing numerical values: ")
    st.sidebar.write(red_numcols)
    st.sidebar.write("Name of columns containing string or non-numerical values: ")
    st.sidebar.write(red_strcols)




if len(red_cols)==1:
    st.write("Please select following variables for different plotting (for reduced dataset)")
    rxv = st.selectbox('(For reduced dataset) Please select x or first variable:', red_cols)
elif len(red_cols)==2:
    st.write("Please select following variables for different plotting (for reduced dataset)")
    rxv = st.selectbox('(For reduced dataset) Please select x or first variable:', red_cols)
    ryv = st.selectbox('(For reduced dataset) Please select y or second variiable:', red_cols)
else:
    st.write("Please select following variables for different plotting (for reduced dataset)")
    rxv = st.selectbox('(For reduced dataset) Please select x or first variable:', red_cols)
    ryv = st.selectbox('(For reduced dataset) Please select y or second variiable:', red_cols)
    rzv = st.selectbox('(For reduced dataset) Please select hue or third variiable:', red_cols)


if len(red_cols)>=2:
    plot1 = plt.figure(figsize=(10, 4))
    sns.lineplot(x=rxv, y=ryv, data=red_df)
    st.pyplot(plot1)

    plot2 = sns.pairplot(red_df)
    st.pyplot(plot2.fig)

    plot3 = sns.heatmap(red_df.corr(), annot=True)
    st.pyplot(plot3.get_figure())

    fig4, ax4 = plt.subplots()
    sns.heatmap(red_df.corr(), ax=ax4,annot=True)
    st.write(fig4)

if len(red_cols)>0:
    if len(red_numcols) >= 2:
        st.write("Linear Regression")
        rrxv1 = st.selectbox(' Please select x or independent variable for linear regression:', red_numcols)
        rryv1 = st.selectbox('(For reduced dataset) Please select y or dependent variable for linear regression:',
                             red_numcols)



        rrxv = red_df[rrxv1].values.reshape(-1, 1)
        rryv = red_df[rryv1].values.reshape(-1, 1)

        regressor = linear_model.LinearRegression()
        regressor.fit(rrxv, rryv)
        y_pred = regressor.predict(rrxv)

        fig, ax = plt.subplots()
        ax.scatter(rrxv, rryv, color='red')
        ax.plot(rrxv, y_pred, color='blue')
        plt.xlabel(f'{rrxv1}', fontsize=18)
        plt.ylabel(f'{rryv1}', fontsize=16)
        plt.title("Linear Regression Plot")

        fig.show()
        st.pyplot(fig)

        buttonreg = st.radio(
            f' Select yes to predict your {rryv1} based on your {rrxv1}',
            ["No","Yes"])



        if buttonreg=="Yes":
            rinp = st.number_input(f"Insert value to predict your {rryv1}", value=None, placeholder=f"Type your {rrxv1}...")
            if rinp != None:
                rpredict = regressor.predict(np.array([rinp]).reshape(-1, 1))
                vall=float(rpredict[0])
                st.write(f"Your {rryv1} is {round(vall,3)} for {rrxv1} value of {rinp}")
















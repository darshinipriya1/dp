import streamlit as st
from streamlit_option_menu import option_menu
name=st.text_input("enter a name")
st.write(name)

age=st.text_input("enter a age")
st.write(age)

city=st.selectbox("select your city",("madurai","dindugal"))

points=st.slider("enter your points",0,100)
st.write(points)

st.multiselect("enter your selection",("madurai","trichy","chennai"))

st.radio("select your gender",("male","female"))
st.table()
st.checkbox("et")
st.table({
    "name":"priya",
    "age":19
})

st.button("sumbit")

with st.sidebar:
     menu=option_menu(
        menu_title="my project",
        options=["home","about","contact"],
        icons=["house","fill-person","person-rolodex"]
    )
    
if menu == "home":
       st.title("home")
       col1,col2 = st.columns(2)
       with col1:
           st.text_input("enter a your name")
       with col2:
            st.text_input("enter your age")
elif menu== "about":
    st.title("about")
else:
    st.title("contact")
    
    
    

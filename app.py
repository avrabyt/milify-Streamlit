import streamlit as st
from millify import millify   # import milify

st.set_page_config(layout="centered",page_title="Millify App",page_icon="💰")
st.markdown("## [Millify](https://github.com/azaitsev/millify) App - Convert long numbers into a human-readable format")
st.text("Millify - Created by [Azaitsev](https://github.com/azaitsev/millify)")

input = st.number_input("Enter a number:", value=0, min_value=0)
st.write("The number you entered is:", input)
t = st.radio("Select a type:", ("Precision", "Prefixes"))  
if t == "Precision":   
    res = millify(input,precision=2)
    st.markdown("## Result")
    st.success("The number you entered can be read as: "+ str(res) )
elif t == "Prefixes":
    prefixes = ['kB', 'MB', 'GB']
    res = millify(input, prefixes=prefixes)
    st.markdown("## Result")
    st.success("The number you entered can be read as: "+ str(res)  )
else:
    pass

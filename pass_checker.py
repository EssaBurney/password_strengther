import streamlit as st
import re


st.set_page_config(page_title="Password Strenght Checker", page_icon="🔑")
st.title("🔐Password Strenght Checker")
st.markdown("""
     Welcome To The  Password Strength Checker!
use this simple tool to check the strength of your password and get suggeestion on how to make it stronger.
                    we will give you the helpful tip to create a ***Strong Password***""")


password = st.text_input("Enter the pasword", type="password")
feedback = []
score=0

if password:
    if len(password) >= 8:
        score+=1
    else:
        feedback.append("❌ Password should be atleast 8 characters long")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score+=1
    else:
        feedback.append("❌Password should be contain both upper and lower case characters.")
        
    if re.search(r'\d', password):
        score+=1
    else:
        feedback.append("❌password should contain atleast 1 digit")
    
    if re.search(r'[!@#$%&]', password):
        score+=1
    else:
        feedback.append('❌ Password should contain atleast 1 special character(!@#$%&)')
        
    if score==4:
        feedback.append("✅ Your password is strong!")
    elif score==3:
        feedback.append("your password is medium strong .It could be stronger")
    else:feedback.append("your password is weak make it stronger")
    
    
    if feedback:
        st.markdown("## Improvement suggestion")
        for tip in feedback:
            st.write(tip)

else:
    st.info("please enter your password to get started.")
    
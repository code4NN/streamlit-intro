import streamlit as st

# sample example
st.header(":green[Method 1 to greet]")
userintput = st.text_input("Enter Name")
if userintput.strip():
    st.text(f"Hare Krishna {userintput}")



# Using button but incomplete
st.header(":green[Method 2 to greet]")
userintput = st.text_input("Enter your Name")
def greetme(name):
    st.text(name)
st.button("Greet",on_click=greetme,args=[userintput])



# Using button
st.header(":green[Method 3 to greet]")
userintput = st.text_input("Name Please")
def greetme(name):
    if name.strip():
        st.session_state['greet_message'] = f"Hare Krishna {name}"

st.button("Greet modified",on_click=greetme,args=[userintput])
if 'greet_message' in st.session_state:
    st.header(st.session_state['greet_message'])

def clear_message():
    st.session_state.pop("greet_message")
st.button('clear text',on_click=clear_message)



# Using button
st.header(":green[Method 4 to greet]")
userintput = st.text_input("Could you enter your Name Please")
def greetme(name):
    if name.strip():
        st.session_state['greet_message'] = f"Hare Krishna {name}"

st.button("Greet final",on_click=greetme,args=[userintput])
if 'greet_message' in st.session_state:
    st.header(st.session_state['greet_message'])
    st.session_state.pop("greet_message")

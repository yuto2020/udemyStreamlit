import streamlit as st
import time



st.title('Welcome to Streamlit!')

st.write('Show progress bar')

'Start!!!'

latest_interatiom = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interatiom.text(f'loading {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('Show something on right Column')

if button:
    right_column.write('You pressed right button')

expander = st.expander("What's expander")
expander.write('This is expander')

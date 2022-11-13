import streamlit as st

st.title("CHECK STATIC FILES")

text_to_repeat = st.text_input("Text to repeat")

times_to_repeat = st.slider("Number of times to repeat", min_value=1, max_value=10)

st.write("TEXT TO REPEAT: " + text_to_repeat)
st.write("TIMES TO REPEAT: " + str(times_to_repeat))


st.download_button(
    "Download",
    data=text_to_repeat * times_to_repeat,
    file_name="repeated_text.txt",
)

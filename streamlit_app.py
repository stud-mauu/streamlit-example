from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title("Hello World")

name = st.text_input("Enter your name")

if st.button("Say Hello"):
    st.write("Hello", name)
    
st.write("Welcome to Chris Daniel B. Cayabyab's \nCombinations generator")
n_read = (st.number_input("Enter number of elements\nn = "))
r = (st.number_input("Enter number of sample\s \nr = "))

if st.button("Generate"):
    chars = [i+1 for i in range(n_read)]
    n = len(chars)

    arr = [i for i in range(r)]
    arr2 = [i for i in range(n+1-r, n+1)]

    n_copy = n
    terminator = n - r + 1

    results = list()

    while(arr[0] < terminator):
        current_list = list()

        for k in range(r):
            current_list.append(chars[arr[k]])

        results.append(current_list)

        # dulo
        i = r - 1
        n_copy = n
        while True:
            if i < 0:
                break
            arr[i] += 1
            if (arr[i] >= arr2[i]):
                i -= 1
            else:
                for j in range(i + 1, r):
                    arr[j] = 1 + arr[j-1]
                break


    stri = " "
    for set in results:
        for char in set:
            stri += str(char) + " " 
        stri += "\n "
    st.write("\nList of " + str(r) + "-combinations of {1,...," + str(n_read) + "}\n\n" + stri + 
    "\nTotal of " + str(len(results)) + " combinations")


import streamlit as st
import time

st.write("""
         # Countdown Timer
         Input your time (in seconds) and start the countdown!
""")

x = st.number_input("Time: ", 0)
start = st.button("Start Countdown")
stop = st.button("Stop Countdown")

if start:
    while True:
        st.write(x)
        x -= 1
        time.sleep(1)
        if x == 0:
            st.success("Countdown Finished!")
            break
        elif x < 0:
            st.write("Invalid.")
            break

if stop:
    st.success("Countdown Finished!")
import streamlit as st
import time
import winsound

st.write("""
         # Countdown Timer
         Input your time (in seconds) and start the countdown!
""")

t = st.number_input("Time: ", 0)
start = st.button("Start Countdown")
stop = st.button("Stop Countdown")

if start:
    with st.empty():
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            st.title(timeformat)
            time.sleep(1)
            t -= 1
            if t == 0:
                st.success("Countdown Finished!")
                winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
                break
            elif t < 0:
                st.write("Invalid.")
                break


if stop:
    st.success("Countdown Stopped")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
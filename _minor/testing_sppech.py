# import speech_recognition as sr
# import streamlit as st  
# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Say something...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#         # add a button to stop listening and print the text that was recognized
#         if st.button("Stop"):
#             break


#     try:
#         text = recognizer.recognize_google(audio)
#         print(f"You said: {text}")
#     except sr.UnknownValueError:
#         print("Sorry, I couldn't understand what you said.")
#     except sr.RequestError as e:
#         print(f"Error with the speech recognition service: {e}")

# if __name__ == "__main__":
#     recognize_speech()


import speech_recognition as sr
import streamlit as st  

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.write(f"You said: {text}")
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        st.write(f"Error with the speech recognition service: {e}")

# Streamlit app
st.title("Speech Recognition App")

if st.button("Start Listening"):
    recognize_speech()

st.markdown("## Instructions:")
st.write("1. Click the 'Start Listening' button.")
st.write("2. Speak into your microphone.")
st.write("3. Click the 'Stop' button to stop listening and see the recognized text.")

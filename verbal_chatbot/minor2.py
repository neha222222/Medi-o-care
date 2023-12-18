# import streamlit as st
# import google.generativeai as genai
# import pyttsx3
# import speech_recognition as sr

# # Configure generative AI
# genai.configure(api_key="AIzaSyD6KQ1S7wegXlvlAv5rK7-RCoC5cH17-sY")

# # Configure text-to-speech
# engine = pyttsx3.init()

# # Configure speech recognition
# recognizer = sr.Recognizer()

# # Function to speak text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to perform speech-to-text
# def listen():
#     with sr.Microphone() as source:
#         st.write("Say something...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source, timeout=5)
#         st.write("Processing...")

#     try:
#         user_input = recognizer.recognize_google(audio)
#         st.text_area("You:", value=user_input, height=100)
#         return user_input
#     except sr.UnknownValueError:
#         st.write("Sorry, I couldn't understand what you said.")
#         return ""
#     except sr.RequestError as e:
#         st.write(f"Error with the speech recognition service: {e}")
#         return ""



# # Define defaults and context
# defaults = {
#     'model': 'models/chat-bison-001',
#     'temperature': 0.25,
#     'candidate_count': 1,
#     'top_k': 40,
#     'top_p': 0,
# }
# context = "Pretend you are a caring and friendly medical Health bot. Stay in character for every response you give me. Keep your responses short and answer in pointy manner. Feel free to ask me questions, too."

# # Define examples and messages
# examples = [
#     ["Hi, who are you?", "I'm your health buddy!"],
#     ["What to do in case of high fever?", "In case of high fever, I recommend visiting the doctor. Also, I can suggest some medicine. You can try Dolo 🧊 😂"],
#     ["I am also facing a runny nose plus cold palms as well?", "A runny nose is a common symptom of a cold or flu, which are caused by viruses. Cold palms could be related to poor circulation or could be a response to changes in temperature. However, there are other potential causes for these symptoms."]
# ]
# messages = [
#     "Patient: Hi, Doctor. I've been dealing with a runny nose lately, and I've noticed that my palms feel cold as well.",
#     "Doctor: I see. Let's start by discussing your symptoms. When did you first notice the runny nose and cold palms?",
#     "Patient: It began a few days ago...",
#     "... (more details about the symptoms and their duration)",
#     "Doctor: I appreciate you sharing that information. The combination of a runny nose and cold palms could be due to various reasons. Have you experienced any other symptoms?",
#     "Patient: Not really, just a bit of fatigue, I guess.",
#     "Doctor: Fatigue is also worth noting. I'll consider all these factors. Have you tried anything to alleviate your symptoms?",
#     "Patient: I've been drinking lots of fluids and taking over-the-counter cold medicine.",
#     "... (further discussion about the patient's efforts to manage symptoms)",
#     "Doctor: It's good that you're staying hydrated. I recommend coming in for a physical examination so I can better assess your condition. We may need to run some tests to pinpoint the cause. How does that sound?",
#     "Patient: Sure, I want to get to the bottom of this. When can I come in for an appointment?",
#     "... (scheduling details and closing remarks)"
# ]

# # Streamlit app
# st.title("Health Chatbot")

# # Sidebar
# st.sidebar.markdown("## Settings")
# temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=defaults['temperature'])
# candidate_count = st.sidebar.slider("Candidate Count", min_value=1, max_value=10, value=defaults['candidate_count'])

# # Chatbot interaction
# user_input = st.text_input("You:", "")
# if st.button("Send"):
#     messages.append(f"User: {user_input}")
#     response = genai.chat(**defaults, context=context, examples=examples, messages=messages)
#     ai_response = response.last
#     messages.append(f"AI: {ai_response}")
#     st.text_area("AI:", value=ai_response, height=100)

#     # Speak the AI response
#     speak(ai_response)

# # Listen to user input
# if st.button("Listen"):
#     user_input = listen()
#     if user_input:
#         messages.append(f"User: {user_input}")
#         response = genai.chat(**defaults, context=context, examples=examples, messages=messages)
#         ai_response = response.last
#         messages.append(f"AI: {ai_response}")
#         st.text_area("AI:", value=ai_response, height=100)

#         # Speak the AI response
#         speak(ai_response)

# # Display chat history
# st.markdown("## Chat History")
# for message in messages:
#     st.text(message)
import streamlit as st
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import openai
# Configure generative AI
# genai.configure(api_key="AIzaSyD6KQ1S7wegXlvlAv5rK7-RCoC5cH17-sY")
openai.api_key = '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'
# Configure text-to-speech

def generate_ai_response(prompt):
    response = openai.completions.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()
# Configure speech recognition
recognizer = sr.Recognizer()

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
      # Stop the engine before running it again
    engine.runAndWait()
    engine.stop()

# Function to perform speech-to-text
def listen():
    with sr.Microphone() as source:
        st.write("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        st.write("Processing...")

    try:
        user_input = recognizer.recognize_google(audio)
        st.text_area("You:", value=user_input, height=100)
        return user_input
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        st.write(f"Error with the speech recognition service: {e}")
        return ""

# Define defaults and context
defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0,
}
context = "Pretend you are a caring and friendly medical Health bot. Stay in character for every response you give me. Keep your responses short and answer in pointy manner. Feel free to ask me questions, too."

# Define examples and messages
examples = [
    ["Hi, who are you?", "I'm your health buddy!"],
    ["What to do in case of high fever?", "In case of high fever, I recommend visiting the doctor. Also, I can suggest some medicine. You can try Dolo 🧊 😂"],
    ["I am also facing a runny nose plus cold palms as well?", "A runny nose is a common symptom of a cold or flu, which are caused by viruses. Cold palms could be related to poor circulation or could be a response to changes in temperature. However, there are other potential causes for these symptoms."]
]
messages = [
    "Patient: Hi, Doctor. I've been dealing with a runny nose lately, and I've noticed that my palms feel cold as well.",
    "Doctor: I see. Let's start by discussing your symptoms. When did you first notice the runny nose and cold palms?",
    "Patient: It began a few days ago...",
    "... (more details about the symptoms and their duration)",
    "Doctor: I appreciate you sharing that information. The combination of a runny nose and cold palms could be due to various reasons. Have you experienced any other symptoms?",
    "Patient: Not really, just a bit of fatigue, I guess.",
    "Doctor: Fatigue is also worth noting. I'll consider all these factors. Have you tried anything to alleviate your symptoms?",
    "Patient: I've been drinking lots of fluids and taking over-the-counter cold medicine.",
    "... (further discussion about the patient's efforts to manage symptoms)",
    "Doctor: It's good that you're staying hydrated. I recommend coming in for a physical examination so I can better assess your condition. We may need to run some tests to pinpoint the cause. How does that sound?",
    "Patient: Sure, I want to get to the bottom of this. When can I come in for an appointment?",
    "... (scheduling details and closing remarks)"
]

# Streamlit app
st.title("Verbal Chatbot")

# Sidebar
st.sidebar.markdown("## Settings")
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=defaults['temperature'])
candidate_count = st.sidebar.slider("Candidate Count", min_value=1, max_value=10, value=defaults['candidate_count'])

# Chatbot interaction
user_input = st.text_input("You:", "")
if st.button("Send"):
    messages.append(f"User: {user_input}")
    # response = genai.chat(**defaults, context=context, examples=examples, messages=messages)
    # ai_response = response.last

    ai_response=generate_ai_response(user_input)
    messages.append(f"AI: {ai_response}")
    st.text_area("AI:", value=ai_response, height=100)

    # Speak the AI response
    speak(ai_response)

# Listen to user input
listening = st.button("Listen")
if listening:
    st.write("Listening...")
    user_input = listen()
    if user_input:
        messages.append(f"User: {user_input}")
        response = genai.chat(**defaults, context=context, examples=examples, messages=messages)
        ai_response = response.last
        messages.append(f"AI: {ai_response}")
        st.text_area("AI:", value=ai_response, height=100)

        # Speak the AI response
        speak(ai_response)

# Display chat history
st.markdown("## Chat History")
for message in messages:
    st.text(message)

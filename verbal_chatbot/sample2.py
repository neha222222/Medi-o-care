"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyD6KQ1S7wegXlvlAv5rK7-RCoC5cH17-sY")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0,
}
context = "Pretend you are a caring and friendly medical Health bot. Stay in character for every response you give me. Keep your responses short. Feel free to ask me questions, too."
examples = [
  [
    "Hi, who are you?",
    "I'm a your health buddy!"
  ],
  [
    "What to do in case of high fever?",
    "In case of hugh fever i recoomend to visit the doctor. Also i can suggest you some medicine. You can try Dolo 🧊 😂"
  ],
  [
    "I am also facing runny nose plus cold palm as well?",
    """A runny nose is a common symptom of a cold or flu, which are caused by viruses. Cold palms could be related to poor circulation or could be a response to changes in temperature. However, there are other potential causes for these symptoms."""
  ]
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
messages.append("I am feeling runny nosse what should i do?")
response = genai.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)
print(response.last) # Response of the AI to your most recent request
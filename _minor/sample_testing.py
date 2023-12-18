from langchain.llms import GooglePalm

def use_google_palm():
    # Replace 'YOUR_GOOGLE_API_KEY' with your actual Google API key
    google_api_key = 'AIzaSyD6KQ1S7wegXlvlAv5rK7-RCoC5cH17-sY'
    
    # Create an instance of the GooglePalm language model
    google_palm = GooglePalm(google_api_key=google_api_key)

    # Input text to generate responses
    input_text = ["I am having high fever what should i do "]

    # Generate a response using the GooglePalm model
    response = google_palm.generate(input_text)
    generated_text = response.generations[0]

    # Print the generated response
    print("Input: ", input_text)
    print("Response: ", generated_text)

if __name__ == "__main__":
    use_google_palm()


api_key = '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'

import openai

def generate_questions(text, num_questions=5):
    # Set your OpenAI API key
    openai.api_key = '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'

    # Use OpenAI GPT-3 to generate questions
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate {num_questions} questions based on the following text:\n{text}\n\n1.",
        max_tokens=150,
        n=1,
        stop=None
    )

    # Extract generated questions from the OpenAI response
    generated_questions = response['choices'][0]['text'].strip().split('\n')[1:]

    # Create a dictionary in the desired format
    questions_dict = {}
    for i, question in enumerate(generated_questions):
        questions_dict[i + 1] = {'question': question, 'options': [], 'correct_answer': ''}

    return questions_dict

# Example usage
if __name__=="__main__":

    input_text = "The quick brown fox jumps over the lazy dog."
    generated_questions_dict = generate_questions(input_text)

    # Print the generated questions dictionary
    for key, value in generated_questions_dict.items():
        print(f"{key}: {value}")

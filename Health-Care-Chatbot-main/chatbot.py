import random
import json
import torch
from fuzzywuzzy import fuzz
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import itertools

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load patterns and intents from JSON file
with open('FINAL_INTENTS.json', 'r') as file:
    data = json.load(file)
    intents = data['intents']

FILE = "TrainingData.pth"
training_data = torch.load(FILE)

input_size = training_data["input_size"]
hidden_size = training_data["hidden_size"]
output_size = training_data["output_size"]
all_words = training_data["all_words"]
tags = training_data["tags"]
model_state = training_data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "MEDIBOT"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                if tag == "goodbye":
                    return reply
                else:
                    return reply
                
    # If no exact match, check for fuzzy matches
    fuzzy_threshold = 80  # Adjust the threshold as needed
    for intent in intents:
        for pattern in intent["patterns"]:
            if fuzz.partial_ratio(msg, pattern) >= fuzzy_threshold:
                reply = random.choice(intent["responses"])
                return reply
            
    return "I do not understand.."



def generate_synonyms(sentence):
    tokens = word_tokenize(sentence)
    synonyms = []
    for token in tokens:
        for syn in wordnet.synsets(token):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
    return list(set(synonyms))

def generate_variations(pattern, max_synonyms_per_word=3):
    synonyms_list = [generate_synonyms(word)[:max_synonyms_per_word] for word in pattern.split()]
    variations = list(itertools.product(*synonyms_list))
    variations.extend([pattern])  # Add the original pattern
    return [' '.join(variation) for variation in variations]

# Generate variations
patterns = [item for sublist in [intent['patterns'] for intent in intents] for item in sublist]
expanded_patterns = [generate_variations(pattern) for pattern in patterns]
flattened_patterns = [item for sublist in expanded_patterns for item in sublist]

# You can use these patterns in your data

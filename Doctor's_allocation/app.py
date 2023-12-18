from flask import Flask, render_template, request
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Sample training data
symptoms_data = [
    ("fever", "Flu"),
    ("cough", "Flu"),
    ("fatigue", "Flu"),
    ("runny_nose", "Flu"),
    ("muscle_pain", "Flu"),
    ("Headache", "Migraine"),
    ("sore_throat", "Flu"),
    ("chills", "Flu"),
    ("nausea", "Food Poisoning"),
    ("vomiting", "Food Poisoning"),
    ("abdominal_pain", "Food Poisoning"),
    ("diarrhea", "Food Poisoning"),
    ("shortness_of_breath", "Asthma"),
    ("Chest pain", "Heart Disease"),
    ("dizziness", "Low Blood Pressure"),
    ("joint_pain", "Rheumatoid Arthritis"),
    ("loss_of_appetite", "Gastroenteritis"),
    ("rash", "Allergic Reaction"),
    ("blurred_vision", "Diabetes"),
    ("difficulty_swallowing", "GERD"),
    ("excessive_thirst", "Diabetes"),
    ("frequent_urination", "Diabetes"),
    ("weight_loss", "Hyperthyroidism"),
    ("numbness", "Multiple Sclerosis"),
    ("confusion", "Alzheimer's Disease"),
    ("irritability", "Depression"),
    ("swollen_glands", "Mononucleosis"),
    ("constipation", "Constipation"),
    ("back_pain", "Herniated Disc"),
    ("drowsiness", "Sleep Apnea"),
    ("abdominal_bloating", "Irritable Bowel Syndrome"),
    ("hair_loss", "Alopecia"),
    ("persistent_cough", "Chronic Bronchitis"),
    ("irregular_heartbeat", "Arrhythmia"),
    ("difficulty_concentrating", "Attention Deficit Hyperactivity Disorder"),
    ("frequent_headaches", "Migraine"),
    ("persistent_back_pain", "Sciatica"),
    ("painful_urination", "Urinary Tract Infection"),
    ("visual_disturbances", "Migraine"),
    ("trouble_swallowing", "Esophageal Cancer"),
    ("skin_changes", "Skin Cancer"),
    # Add more training samples as needed
]

# Convert symptoms and labels to vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([symptom[0] for symptom in symptoms_data])
y = [label[1] for label in symptoms_data]

# Train a simple Random Forest Classifier
model = RandomForestClassifier()
model.fit(X, y)

def predict_disease(symptoms):
    symptoms_vector = vectorizer.transform(symptoms)
    return model.predict(symptoms_vector)[0]

def recommend_doctor_osm_api(disease):
    # Coordinates for India (latitude, longitude)
    india_coordinates = "20.5937,78.9629"

    # Mapping of diseases to specialist doctors
    specialist_mapping = {
        "Flu": "Physician",
        "Food Poisoning": "Gastroenterologist",
        "Asthma": "Pulmonologist",
        "Heart Disease": "Cardiologist",
        "Low Blood Pressure": "Cardiologist",
        "Rheumatoid Arthritis": "Rheumatologist",
        "Gastroenteritis": "Gastroenterologist",
        "Allergic Reaction": "Allergist",
        "Diabetes": "Endocrinologist",
        "GERD": "Gastroenterologist",
        "Hyperthyroidism": "Endocrinologist",
        "Multiple Sclerosis": "Neurologist",
        "Alzheimer's Disease": "Neurologist",
        "Depression": "Psychiatrist",
        "Mononucleosis": "Infectious Disease Specialist",
        "Constipation": "Gastroenterologist",
        "Herniated Disc": "Orthopedic Surgeon",
        "Sleep Apnea": "Sleep Specialist",
        # Add more mappings as needed
    }

    # Get the specialist for the given disease
    specialist = specialist_mapping.get(disease, "Unknown Specialist")

    # Simulating a search for doctors based on the predicted disease in India
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{specialist}",
        "format": "json",
        "addressdetails": 1,
        "viewbox": "68.1,6.8,97.4,35.7",  # Set the viewbox for India and nearby
        "bounded": 1
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extracting detailed information about doctors from the API response
    doctors = []
    for result in data:
        doctor_info = {
            "name": result.get("display_name", "Unknown Doctor"),
            "address": result.get("address", {}).get("road", "Unknown Address"),
            "city": result.get("address", {}).get("city", "Unknown City"),
            "country": result.get("address", {}).get("country", "Unknown Country")
        }
        doctors.append(doctor_info)

    return doctors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form.get('symptoms')
    predicted_disease = predict_disease(symptoms.split(','))
    recommended_doctors = recommend_doctor_osm_api(predicted_disease)
    return render_template('result.html', predicted_disease=predicted_disease, recommended_doctors=recommended_doctors)

# Add routes for additional pages
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/healthbot')
def healthbot():
    return render_template('healthbot.html')

@app.route('/allocation')
def allocation():
    return render_template('allocation.html')

if __name__ == '__main__':
    app.run(debug=True)

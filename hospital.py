import json

# Define the knowledge base
knowledge_base = {
    "fever": {
        "symptoms": ["fever", "chills", "sweating", "headache", "muscle aches", "sore throat", "cough"],
        "treatments": ["rest", "plenty of fluids", "over-the-counter medications", "see a doctor if symptoms are severe"],
    },
    "chest pain": {
        "symptoms": ["chest pain", "shortness of breath", "nausea", "dizziness", "sweating"],
        "treatments": ["rest", "call 911 if symptoms are severe"],
    },
    "broken bones": {
        "symptoms": ["pain", "swelling", "bruising", "deformity"],
        "treatments": ["splint or cast", "surgery","see a doctor if symptoms are severe"],
    },
    "stomach pain": {
        "symptoms": ["stomach pain", "nausea", "vomiting", "diarrhea"],
        "treatments": ["over-the-counter medications", "see a doctor if symptoms are severe"],
    },
}

# Define the decision tree
def decision_tree(symptoms):
    for symptom in symptoms:
        if symptom in knowledge_base:
            return knowledge_base[symptom]["treatments"]
    return "Please consult a doctor."

# Ask the user to enter their symptoms
symptoms = input("What symptoms are you experiencing? (comma-separated) ")
symptoms = symptoms.split(",")

# Call the decision tree function
treatments = decision_tree(symptoms)

# Print the recommended treatments
print("Here are the recommended treatments for your symptoms:", treatments)

# Recommend hospitals
def recommend_hospitals(symptoms):
    hospitals = []
    for symptom in symptoms:
        for hospital in hospitals_by_symptom[symptom]:
            hospitals.append(hospital)
            break
    return hospitals

# Define the hospitals by symptom
hospitals_by_symptom = {
    "fever": ["Johns Hopkins Hospital", "Mayo Clinic", "Cleveland Clinic"],
    "chills": ["Johns Hopkins Hospital", "Mayo Clinic", "Cleveland Clinic"],
    "chest pain": ["Memorial Sloan Kettering Cancer Center", "Stanford University Medical Center", "Massachusetts General Hospital"],
    "broken bones": ["Children's Hospital of Philadelphia", "Texas Children's Hospital", "St. Jude Children's Research Hospital"],
    "stomach pain": ["University of Chicago Medicine", "Columbia University Irving Medical Center", "New York-Presbyterian Hospital"],
}

# Call the recommend_hospitals function
hospitals = recommend_hospitals(symptoms)

# Print the recommended hospitals
print("Here are some recommended hospitals for your symptoms:", hospitals)